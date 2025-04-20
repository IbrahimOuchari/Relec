
from odoo import fields, models


class ResCompany(models.Model):

    _inherit = "res.company"

    purchase_manual_delivery = fields.Boolean(
        string="Réception Manuelle des Achats", required=False
    )
