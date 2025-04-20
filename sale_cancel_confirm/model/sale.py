
from odoo import models


class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = ["sale.order", "base.cancel.confirm"]

    _has_cancel_reason = "required"  # ["no", "optional", "required"]

    def action_cancel(self):
        if not self.filtered("cancel_confirm"):
            return self.open_cancel_confirm_wizard()
        return super().action_cancel()

    def action_draft(self):
        self.clear_cancel_confirm_data()
        return super().action_draft()
