from odoo import api, fields, models, _

### create a new class for Top Selling Products with Quantity
class TopsellingProducts(models.Model):
    _name = "sale.quantity"
    _order = 'quantity desc'
    _description = 'Sale Quantity'

    product = fields.Many2one('product.product', string ='Produit')
    quantity = fields.Float(string ='Quantité')

