from odoo import api,fields,models,_

class AddQuotationCancelReason(models.TransientModel):
    _name="add.quotation.reason"
    _description = "Add Quotation Reason"
 
    quota_cancel_reason_id = fields.Many2one("quotation.cancel.reason",string= "Motif d'Annulation Devis", required =True, help="Ce champ affiche la raison de l'annulation du devis")

    # For adding the reason of cancel quotation on sales quotation	
    def cancel_quotation(self):
        if self.env.context.get('active_model') == 'sale.order':
            active_model_id = self.env.context.get('active_id')
            sale_obj = self.env['sale.order'].search([('id','=',active_model_id)])
            sale_obj.write({'quota_cancel_reason_id':self.quota_cancel_reason_id.id, 'state':'cancel'})
