# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_customer = fields.Boolean(string='Client',
                                help="Cochez cette case si ce contact est un client. Il peut être sélectionné dans les commandes clients.")
    is_supplier = fields.Boolean(string='Fournisseur',
                                help="Cochez cette case si ce contact est un fournisseur. Il peut être sélectionné dans les bons de commande.")
    