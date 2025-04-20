from odoo import api, fields, models
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    _description = "Bon de Commande"

    mrp_production_count = fields.Char()

    total_sans_remise = fields.Monetary(string='Montant Total', store=True, readonly=True, compute='_total_sans_remise',
                                        tracking=5)

    @api.depends('order_line.prix_remise')
    def _total_sans_remise(self):
        for order in self:
            total_sans_remise = 0.0
            for line in order.order_line:
                total_sans_remise += line.prix_remise
            order.update({
                'total_sans_remise': total_sans_remise,

            })

    class SaleOrdeLine(models.Model):
        _inherit = "sale.order.line"
        _description = "Sales Line Management"

        poste = fields.Char(string="N° Poste")
        ref_product_client_id = fields.Char('product.template', related="product_id.ref_product_client")

        ref_client_id = fields.Char('sale.order', domain="[('partner_id', '=', partner_id)]",
                                    related="order_id.ref_client")

        status_bc = fields.Selection('sale.order', related="order_id.picking_status")

        prix_remise = fields.Float(string='Total', digits='Product Price', compute="_compute_price_remise")

        pu_avec_remise = fields.Float(string='P.U. Après Remise', digits='Product Price', readonly=True,
                                      compute='_pu_avec_remise', )

        qty_restante = fields.Float(string='Qte Restante', digits='Product Unit of Measure',
                                    compute="_compute_qte_restante")

        @api.depends("product_uom_qty", "qty_delivered")
        def _compute_qte_restante(self):
            for line in self:
                line.qty_restante = line.product_uom_qty - line.qty_delivered

        @api.depends('product_uom_qty', 'price_unit')
        def _compute_price_remise(self):
            for compute in self:
                compute.prix_remise = compute.product_uom_qty * compute.price_unit

        @api.depends('discount', 'price_unit')
        def _pu_avec_remise(self):
            for compute in self:
                compute.pu_avec_remise = ((100 - compute.discount) / 100) * compute.price_unit

    class StockPicking(models.Model):
        _inherit = "stock.picking"

        ref_client_id = fields.Char('sale.order', domain="[('partner_id', '=', partner_id)]",
                                    related="sale_id.ref_client")

        operation_fourni = fields.Selection(related='picking_type_id.operation_fourni')

    class PickingType(models.Model):
        _inherit = "stock.picking.type"

        operation_fourni = fields.Selection([('fourni', 'Opération Fourni'), ('retour', 'Opération Retour')])

    class StockPickingline(models.Model):
        _inherit = "stock.move"
        _description = "Stock Picking"

        picking_type_code = fields.Selection(related='picking_id.picking_type_code')
        operation_fourni = fields.Selection(related='picking_id.operation_fourni')

        price_id = fields.Float(readonly=True, related="sale_line_id.price_unit")

        poste_id = fields.Char(readonly=True, related="sale_line_id.poste")
        sale_order_line = fields.Many2one()
        sale_id = fields.Many2one()
        ref_product_client_id = fields.Char('product.template', related="product_id.ref_product_client")
        description_sale_id = fields.Text('product.template', related="product_id.description_sale")

    class ProductProduct(models.Model):
        _inherit = "product.product"

    client_id = fields.Many2one('product.template', 'product_id.client_id')
