
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    sale_discount = fields.Float(
        string="Remise Client",
        digits="Discount",
        company_dependent=True,
    )
