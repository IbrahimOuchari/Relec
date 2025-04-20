
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class srPurchasePriceHistory(models.Model):
    _name = 'sr.purchase.price.history'
    _description = 'Purchase Price History'

    name = fields.Many2one("purchase.order.line",string="Ligne de BC Achat")
    partner_id = fields.Many2one("res.partner",string="Fournisseur")
    user_id = fields.Many2one("res.users",string="Responsable Achat")
    product_tmpl_id = fields.Many2one("product.template",string="Template Id")
    variant_id = fields.Many2one("product.product",string="Produit")
    purchase_order_id = fields.Many2one("purchase.order",string="BC Achat")
    purchase_order_date = fields.Datetime(string="Date BC Achat")
    product_uom_qty = fields.Float(string="Quantité", digits='Product Unit of Measure')
    unit_price = fields.Float(string="Prix", digits='Product Price')
    currency_id = fields.Many2one("res.currency",string="Devise")
    total_price = fields.Monetary(string="Total", digits='Product Price')

