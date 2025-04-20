# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    order_ref = fields.Char('Order Reference',related='order_id.name')   
    vendor_id = fields.Many2one('res.partner',related='order_id.partner_id')


