
from odoo import api, fields, models


class StockMove(models.Model):
    _name = "stock.move"
    _inherit = [
        _name,
        "stock.invoice.state.mixin",
    ]

    def _get_taxes(self, fiscal_position, inv_type):
        """
        Map product taxes based on given fiscal position
        :param fiscal_position: account.fiscal.position recordset
        :param inv_type: string
        :return: account.tax recordset
        """
        product = self.mapped("product_id")
        product.ensure_one()
        if inv_type in ("out_invoice", "out_refund"):
            taxes = product.taxes_id
        else:
            taxes = product.supplier_taxes_id
        company_id = self.env.context.get("force_company", self.env.user.company_id.id)
        my_taxes = taxes.filtered(lambda r: r.company_id.id == company_id)
        return fiscal_position.map_tax(my_taxes)

    @api.model
    def _get_account(self, fiscal_position, account):
        """
        Map the given account with given fiscal position
        :param fiscal_position: account.fiscal.position recordset
        :param account: account.account recordset
        :return: account.account recordset
        """
        return fiscal_position.map_account(account)

    def _get_price_unit_invoice(self, inv_type, partner, qty=1):
        """
        Gets price unit for invoice
        :param inv_type: str
        :param partner: res.partner
        :param qty: float
        :return: float
        """
        product = self.mapped("product_id")
        product.ensure_one()
        if inv_type in ("in_invoice", "in_refund"):
            result = product.price
        else:
            # If partner given, search price in its sale pricelist
            if partner and partner.property_product_pricelist:
                product = product.with_context(
                    partner=partner.id,
                    quantity=qty,
                    pricelist=partner.property_product_pricelist.id,
                    uom=fields.first(self).product_uom.id,
                )
                result = product.price
            else:
                result = product.lst_price
        return result

    def _prepare_extra_move_vals(self, qty):
        """Copy invoice state for a new extra stock move"""
        values = super()._prepare_extra_move_vals(qty)
        values["invoice_state"] = self.invoice_state
        return values

    def _prepare_move_split_vals(self, uom_qty):
        """Copy invoice state for a new splitted stock move"""
        values = super()._prepare_move_split_vals(uom_qty)
        values["invoice_state"] = self.invoice_state
        return values
