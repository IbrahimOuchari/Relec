
from odoo import fields, models


class ResConfigSettings(models.TransientModel):

    _inherit = "res.config.settings"

    purchase_manual_delivery = fields.Boolean(
        related="company_id.purchase_manual_delivery", readonly=False
    )
