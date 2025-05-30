
from odoo import fields, models


class PickingType(models.Model):
    _inherit = "stock.picking.type"

    count_picking_2binvoiced = fields.Integer(compute="_compute_picking_2binvoiced")

    def _compute_picking_2binvoiced(self):
        domains = {
            "count_picking_2binvoiced": [("invoice_state", "=", "2binvoiced")],
        }
        for field in domains:
            data = self.env["stock.picking"].read_group(
                domains[field]
                + [
                    ("state", "!=", "cancel"),
                    ("invoice_state", "=", "2binvoiced"),
                    ("picking_type_id", "in", self.ids),
                ],
                ["picking_type_id"],
                ["picking_type_id"],
            )
            count = {
                x["picking_type_id"][0]: x["picking_type_id_count"]
                for x in data
                if x["picking_type_id"]
            }
            for record in self:
                record[field] = count.get(record.id, 0)
