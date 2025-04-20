
from odoo import models


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = ["purchase.order", "base.cancel.confirm"]

    _has_cancel_reason = "required"  # ["no", "optional", "required"]

    def button_cancel(self):
        if not self.filtered("cancel_confirm"):
            return self.open_cancel_confirm_wizard()
        return super().button_cancel()

    def button_draft(self):
        self.clear_cancel_confirm_data()
        return super().button_draft()
