from odoo import api,fields,models,_

#inherit SaleOrder class.
class SaleOrder(models.Model):
    _inherit = "sale.order"

    discount_total = fields.Monetary("Total Remise",compute='total_discount')

    #Count for total discount
    @api.depends('order_line.product_uom_qty','order_line.price_unit','order_line.discount')
    def total_discount(self):
        for order in self:
            total_price = 0
            discount_amount = 0
            final_discount_amount = 0
            if order:  
                for line in order.order_line:
                    if line:
                        total_price = line.product_uom_qty * line.price_unit
                        if total_price:  
                            discount_amount = total_price - line.price_subtotal
                            if discount_amount: 
                                final_discount_amount = final_discount_amount + discount_amount
                order.update({'discount_total':final_discount_amount})

