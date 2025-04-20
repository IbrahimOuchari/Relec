from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    _description = "Product Template"

    fourni = fields.Boolean(string="Produit Fourni", default=False)
    produit_fini = fields.Boolean(string="Produit Fini", default=False)
    sale_ok = fields.Boolean('Can be Sold', default=False)
    purchase_ok = fields.Boolean('Can be Purchased', default=False)
    client_id = fields.Many2one('res.partner', string="Client", domain = "[('is_customer','=',True)]", store=True,)
    ref_product_client = fields.Char(string="Référence Client")
