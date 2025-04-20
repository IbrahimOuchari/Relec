
from odoo import api,fields,models,_

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    quota_cancel_reason_id = fields.Many2one("quotation.cancel.reason",string= "Motif d'Annulation du Présent Devis",help="Ce champ affiche la raison de l'annulation du devis")
    
    # action_cancel function return wizard
    def action_cancel(self,context=None):
        return {
        'name': ('Annulation'),
        'view_type': 'form',
        'view_mode': 'form',
        'res_model': 'add.quotation.reason',
        'view_id': False,
        'type': 'ir.actions.act_window',
        'target':'new'
    	}
