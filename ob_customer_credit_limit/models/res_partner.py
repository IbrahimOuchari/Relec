# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_check = fields.Boolean('Activer Limitation de Crédit', help='Activate the credit limit feature')
    credit_warning = fields.Monetary('Montant Avertissement')
    credit_blocking = fields.Monetary('Montant de blocage')
    amount_due = fields.Monetary('Montant Dû', compute='_compute_amount_due')

    @api.depends('credit')
    def _compute_amount_due(self):
        for rec in self:
            rec.amount_due = rec.credit

    @api.constrains('credit_warning', 'credit_blocking')
    def _check_credit_amount(self):
        for credit in self:
            if credit.credit_warning > credit.credit_blocking:
                raise ValidationError(_('Le montant avertissement ne doit pas être supérieur au montant de blocage.'))
            if credit.credit_warning < 0 or credit.credit_blocking < 0:
                raise ValidationError(_('Le montant avertissement ou le montant de blocage ne doit pas être inférieur à zéro.'))
