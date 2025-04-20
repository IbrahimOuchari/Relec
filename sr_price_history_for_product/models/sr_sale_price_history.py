
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class srSalePriceHistory(models.Model):
    _name = 'sr.sale.price.history'
    _description = 'Sale Price History'

    name = fields.Many2one("sale.order.line",string="Lignes de BC Vente")
    partner_id = fields.Many2one("res.partner",string="Client")
    user_id = fields.Many2one("res.users",string="Chargé Client")
    product_tmpl_id = fields.Many2one("product.template",string="Template Id")
    variant_id = fields.Many2one("product.product",string="Produit")
    sale_order_id = fields.Many2one("sale.order",string="BC Vente")
    sale_order_date = fields.Datetime(string="Date BC Vente")
    product_uom_qty = fields.Float(string="Quantité", digits='Product Unit of Measure')
    unit_price = fields.Float(string="Prix", digits='Product Price')
    currency_id = fields.Many2one("res.currency",string="Devise")
    total_price = fields.Monetary(string="Total", digits='Product Price')


