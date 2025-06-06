

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductPricelistPrint(models.TransientModel):
    _name = "product.pricelist.print"
    _description = "Product Pricelist Print"

    context_active_model = fields.Char(
        store=False, compute="_compute_context_active_model"
    )
    pricelist_id = fields.Many2one(comodel_name="product.pricelist", string="Liste des Prix")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Clients")
    partner_ids = fields.Many2many(comodel_name="res.partner", string="Clients")
    categ_ids = fields.Many2many(comodel_name="product.category", string="Catégories")
    show_variants = fields.Boolean()
    product_tmpl_ids = fields.Many2many(
        comodel_name="product.template",
        string="Templates Produits",
        help="Garder vide pour tous les produits",
    )
    product_ids = fields.Many2many(
        comodel_name="product.product",
        string="Produits",
        help="Garder vide pour tous les produits",
    )
    show_standard_price = fields.Boolean(string="Afficher le Prix de Revient")
    show_sale_price = fields.Boolean(string="Afficher le Prix de Vente")
    hide_pricelist_name = fields.Boolean(string="Masquer le Nom de la Liste de Prix")
    order_field = fields.Selection(
        [("name", "Nom"), ("default_code", "Référence Interne")], string="Commande"
    )
    partner_count = fields.Integer(compute="_compute_partner_count")
    date = fields.Date()
    last_ordered_products = fields.Integer(
        help="Si vous entrez un nombre X ici, alors, pour chaque client sélectionné, "
         " les X derniers produits commandés seront obtenus pour le rapport."
    )

    @api.depends("partner_ids")
    def _compute_partner_count(self):
        for record in self:
            self.partner_count = len(record.partner_ids)

    @api.onchange("partner_ids")
    def _onchange_partner_ids(self):
        if not self.partner_count:
            self.last_ordered_products = False

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        if self.env.context.get("active_model") == "product.template":
            res["product_tmpl_ids"] = [(6, 0, self.env.context.get("active_ids", []))]
        elif self.env.context.get("active_model") == "product.product":
            res["show_variants"] = True
            res["product_ids"] = [(6, 0, self.env.context.get("active_ids", []))]
        elif self.env.context.get("active_model") == "product.pricelist":
            res["pricelist_id"] = self.env.context.get("active_id", False)
        elif self.env.context.get("active_model") == "res.partner":
            active_ids = self.env.context.get("active_ids", [])
            res["partner_ids"] = [(6, 0, active_ids)]
            if len(active_ids) == 1:
                partner = self.env["res.partner"].browse(active_ids[0])
                res["pricelist_id"] = partner.property_product_pricelist.id
        elif self.env.context.get("active_model") == "product.pricelist.item":
            active_ids = self.env.context.get("active_ids", [])
            items = self.env["product.pricelist.item"].browse(active_ids)
            # Set pricelist if all the items belong to the same one
            if len(items.mapped("pricelist_id")) == 1:
                res["pricelist_id"] = items[0].pricelist_id.id
            product_items = items.filtered(
                lambda x: x.applied_on == "0_product_variant"
            )
            template_items = items.filtered(lambda x: x.applied_on == "1_product")
            category_items = items.filtered(
                lambda x: x.applied_on == "2_product_category"
            )
            # Convert all pricelist items to their affected variants
            if product_items:
                res["show_variants"] = True
                product_ids = product_items.mapped("product_id")
                product_ids |= template_items.mapped(
                    "product_tmpl_id.product_variant_ids"
                )
                product_ids |= product_ids.search(
                    [
                        ("sale_ok", "=", True),
                        ("categ_id", "in", category_items.mapped("categ_id").ids),
                    ]
                )
                res["product_ids"] = [(6, 0, product_ids.ids)]
            # Convert all pricelist items to their affected templates
            if template_items and not product_items:
                product_tmpl_ids = template_items.mapped("product_tmpl_id")
                product_tmpl_ids |= product_tmpl_ids.search(
                    [
                        ("sale_ok", "=", True),
                        ("categ_id", "in", category_items.mapped("categ_id").ids),
                    ]
                )
                res["product_tmpl_ids"] = [(6, 0, product_tmpl_ids.ids)]
            # Only category items, we just set the categories
            if category_items and not product_items and not template_items:
                res["categ_ids"] = [(6, 0, category_items.mapped("categ_id").ids)]
        return res

    def print_report(self):
        if not (
            self.pricelist_id
            or self.partner_count
            or self.show_standard_price
            or self.show_sale_price
        ):
            raise ValidationError(
                _(
                    "You must set price list or any customer "
                    "or any show price option."
                )
            )
        return self.env.ref(
            "product_pricelist_direct_print." "action_report_product_pricelist"
        ).report_action(self)

    def action_pricelist_send(self):
        self.ensure_one()
        if self.partner_count > 1:
            self.send_batch()
            return
        if self.partner_count == 1:
            partner = self.partner_ids[0]
            self.write(
                {
                    "partner_id": partner.id,
                    "pricelist_id": partner.property_product_pricelist.id,
                }
            )
        return self.message_composer_action()

    def message_composer_action(self):
        self.ensure_one()

        template_id = self.env.ref(
            "product_pricelist_direct_print.email_template_edi_pricelist"
        ).id
        compose_form_id = self.env.ref("mail.email_compose_message_wizard_form").id
        ctx = {
            "default_composition_mode": "comment",
            "default_res_id": self.id,
            "default_model": "product.pricelist.print",
            "default_use_template": bool(template_id),
            "default_template_id": template_id,
        }
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "mail.compose.message",
            "view_id": compose_form_id,
            "target": "new",
            "context": ctx,
        }

    def send_batch(self):
        self.ensure_one()
        for partner in self.partner_ids.filtered(lambda x: not x.parent_id):
            self.write(
                {
                    "partner_id": partner.id,
                    "pricelist_id": partner.property_product_pricelist.id,
                }
            )
            self.force_pricelist_send()

    def force_pricelist_send(self):
        template_id = self.env.ref(
            "product_pricelist_direct_print.email_template_edi_pricelist"
        ).id
        composer = (
            self.env["mail.compose.message"]
            .with_context(
                {
                    "default_composition_mode": "mass_mail",
                    "default_notify": True,
                    "default_res_id": self.id,
                    "default_model": "product.pricelist.print",
                    "default_template_id": template_id,
                    "active_ids": self.ids,
                }
            )
            .create({})
        )
        values = composer.onchange_template_id(
            template_id, "mass_mail", "product.pricelist.print", self.id
        )["value"]
        composer.write(values)
        composer.send_mail()

    def get_last_ordered_products_to_print(self):
        self.ensure_one()
        partner = self.partner_id
        if not partner and self.partner_count == 1:
            partner = self.partner_ids[0]
        orders = partner.sale_order_ids.filtered(
            lambda r: r.state not in ["draft", "sent", "cancel"]
        )
        orders = orders.sorted(key=lambda r: r.date_order, reverse=True)
        products = orders.mapped("order_line").mapped("product_id")
        return products[: self.last_ordered_products]

    def get_pricelist_to_print(self):
        self.ensure_one()
        pricelist = self.pricelist_id
        if not pricelist and self.partner_count == 1:
            pricelist = self.partner_ids[0].property_product_pricelist
        return pricelist

    def _compute_context_active_model(self):
        self.context_active_model = self.env.context.get("active_model")
