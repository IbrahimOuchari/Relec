# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import tools


class StockMoveLineInherit(models.Model):
    _inherit = 'stock.move.line'

    user_sml = fields.Char(string="User", related='create_uid.name', store=True, readonly=True)


