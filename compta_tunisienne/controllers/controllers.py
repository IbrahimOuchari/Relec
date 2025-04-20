# -*- coding: utf-8 -*-
from odoo import http

# class TunisianAccounting(http.Controller):
#     @http.route('/tunisian_accounting/tunisian_accounting/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tunisian_accounting/tunisian_accounting/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tunisian_accounting.listing', {
#             'root': '/tunisian_accounting/tunisian_accounting',
#             'objects': http.request.env['tunisian_accounting.tunisian_accounting'].search([]),
#         })

#     @http.route('/tunisian_accounting/tunisian_accounting/objects/<model("tunisian_accounting.tunisian_accounting"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tunisian_accounting.object', {
#             'object': obj
#         })