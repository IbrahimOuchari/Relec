# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import api, fields, models
from datetime import datetime


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.multi
    def _compute_amount_in_word(self):
        for rec in self:
            #rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total)) + ' only'
            rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total))+ '.'

    num_word = fields.Char(string="Montant en lettres :", compute='_compute_amount_in_word')


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    # @api.multi
    def _compute_amount_in_word(self):
        for rec in self:
            #rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total)) + ' only'
            rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total))+ '.'

    num_word = fields.Char(string="Montant en lettres :", compute='_compute_amount_in_word')


class InvoiceOrder(models.Model):
    _inherit = 'account.move'

    num_word = fields.Char(string="Montant en lettres :", compute='_compute_amount_in_word')

    # @api.multi
    def _compute_amount_in_word(self):
        self.num_word = ""
        for rec in self:
            #rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total)) + ' only'
            rec.num_word = str(rec.currency_id.amount_to_text(rec.amount_total))+ '.'
