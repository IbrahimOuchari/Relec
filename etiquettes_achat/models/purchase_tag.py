
from odoo import api,fields,models,_

class PurchaseTagMenu(models.Model):
    _name ='purchase.tag'
    _description = 'Purchase Tag'

    name = fields.Char(string="Etiquettes Achat") #Added one field to enter purchase tag
    
    
    


