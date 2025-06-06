
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # In core this a related field. We need to trigger its value on view, so we can
    # have it even when we're in a NewId
    order_partner_id = fields.Many2one(depends=["product_id"])
