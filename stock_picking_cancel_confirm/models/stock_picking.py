
from odoo import models


class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = ["stock.picking", "base.cancel.confirm"]

    _has_cancel_reason = "required"  # ["no", "optional", "required"]

    def action_cancel(self):
        if not self.filtered("cancel_confirm"):
            return self.open_cancel_confirm_wizard()
        return super().action_cancel()
