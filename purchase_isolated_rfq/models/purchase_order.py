
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    order_sequence = fields.Boolean(string="Séquence de Commande", readonly=True, index=True)
    quote_id = fields.Many2one(
        comodel_name="purchase.order",
        string="Demande de Prix",
        readonly=True,
        ondelete="restrict",
        copy=False,
        help="Pour le bon de commande, ce champ fait référence à sa demande de prix",
    )
    purchase_order_id = fields.Many2one(
        comodel_name="purchase.order",
        string="N° BC Achat",
        readonly=True,
        ondelete="restrict",
        copy=False,
        help="Pour la demande d'achat, ce champ fait référence à son bon de commande",
    )
    rfq_state = fields.Selection(
        string="Status D.A.",
        readonly=True,
        related="state",
        help="Relative à la demande d'achat",
    )

    @api.model
    def create(self, vals):
        order_sequence = vals.get("order_sequence") or self.env.context.get(
            "order_sequence"
        )
        if not order_sequence and vals.get("name", "/") == "/":
            vals["name"] = self.env["ir.sequence"].next_by_code("purchase.rfq") or "/"
        return super().create(vals)

    def _prepare_order_from_rfq(self):
        return {
            "name": self.env["ir.sequence"].next_by_code("purchase.order") or "/",
            "order_sequence": True,
            "quote_id": self.id,
            "partner_ref": self.partner_ref,
        }

    def action_convert_to_order(self):
        self.ensure_one()
        if self.order_sequence:
            raise UserError(_("Seul les demandes de prix peut être converti en commande"))
        purchase_order = self.copy(self._prepare_order_from_rfq())
        purchase_order.button_confirm()
        # Reference from this RFQ to Purchase Order
        self.purchase_order_id = purchase_order.id
        if self.state == "draft":
            self.button_done()
        return self.open_duplicated_purchase_order()

    @api.model
    def open_duplicated_purchase_order(self):
        return {
            "name": _("Purchases Order"),
            "view_mode": "form",
            "view_id": False,
            "res_model": "purchase.order",
            "context": {"default_order_sequence": True, "order_sequence": True},
            "type": "ir.actions.act_window",
            "nodestroy": True,
            "target": "current",
            "domain": "[('order_sequence', '=', True)]",
            "res_id": self.purchase_order_id and self.purchase_order_id.id or False,
        }
