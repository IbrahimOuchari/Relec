
from odoo import api, fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    contains_unreserved = fields.Boolean(
        string="Contains unreserved products",
        compute="_compute_contains_unreserved",
        store=True,
    )

    @api.depends("quantity", "reserved_quantity")
    def _compute_contains_unreserved(self):
        for record in self:
            # Avoid error when adding a new line on manually Update Quantity
            if isinstance(record.id, models.NewId):
                record.contains_unreserved = False
                continue
            record.contains_unreserved = (
                True if record.available_quantity > 0 else False
            )
