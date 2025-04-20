
from odoo import api,fields,models,_

class PurchaseOrder(models.Model):
    _inherit ='purchase.order'  #This class is inherited because we have to get multiple purchase tag 

    tag_ids = fields.Many2many('purchase.tag',string="Etiquettes Achat") #define Many2many fields to display multiple purchase tags

    ### New Code
    # overload this function to set purchase order tags in invoice.
    def _prepare_invoice(self):
        invoice_vals = super(PurchaseOrder, self)._prepare_invoice()
        invoice_vals.update({'vendor_tag_ids' : [(6, 0, self.tag_ids.ids)]})
        return invoice_vals



