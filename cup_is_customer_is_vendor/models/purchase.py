# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    READONLY_STATES = {
        'purchase': [('readonly', True)],
        'done': [('readonly', True)],
        'cancel': [('readonly', True)],
    }

    partner_id = fields.Many2one(
        'res.partner', string='Fournisseur', required=True, 
        states=READONLY_STATES, change_default=True, 
        tracking=True, domain="[('is_supplier','=',True)]", help="Vous pouvez rechercher un fournisseur par son nom, son adresse e-mail ou sa référence interne.")
    