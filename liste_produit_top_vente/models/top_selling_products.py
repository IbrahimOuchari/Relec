from odoo import api, fields, models, _

### create new class for Top Selling Products with amount
class TopsellingProducts(models.Model):
    _name = "sale.products"
    _order = 'amount desc'
    _description = 'Sale Products'

    product = fields.Many2one('product.product', string='Produit')
    amount = fields.Float(string='Valeur')

