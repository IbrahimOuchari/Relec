

from odoo import api, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.onchange("product_id")
    def _onchange_product_id(self):
        res = super()._onchange_product_id()
        if self.product_id and self.user_has_groups(
            "description_facture_produit."
            "group_use_product_description_per_inv_line"
        ):
            product = self.product_id.with_context(lang=self.move_id.partner_id.lang)
            if self.move_id.is_purchase_document():
                self.name = product.description_purchase or self.name
            elif self.move_id.is_sale_document():
                self.name = product.description_sale or self.name
        return res
