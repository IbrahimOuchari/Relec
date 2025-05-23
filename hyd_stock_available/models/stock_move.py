from odoo import api, fields, models


class StockMove(models.Model):

    _inherit = "stock.move"
    _name = "stock.move"

    not_reserved = fields.Float(
        string="Non réservé",
        compute="_compute_available_qty",
        store=True,
        readonly=True,
    )

    @api.depends("product_id", "product_uom_qty")
    def _compute_available_qty(self):
        for record in self:
            if record.product_id and record.state != "done":
                actual_qty = record.product_id.with_context(
                    {"location": record.location_id.id}
                ).qty_available
                outgoing_qty = record.product_id.with_context(
                    {"location": record.location_id.id}
                ).outgoing_qty
                record.not_reserved = actual_qty - outgoing_qty
