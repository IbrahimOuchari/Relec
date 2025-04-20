
from odoo import api,fields,models,_

class QuotationCancelReason(models.Model):
    _name = "quotation.cancel.reason"
    _description = "Motif d'Annulation Devis"

    name = fields.Char(string='Motif Annulation',help="Pour ajouter le motif de l'annulation du devis.")
