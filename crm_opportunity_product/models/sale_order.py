# -*- coding: utf-8 -*-


from odoo import api, fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    opportunity_id = fields.Many2one('crm.lead',string='Produits pour Devis')
    
    def _prepare_sale_order_lines_from_opportunity(self, record):
        data = {
                    'product_id':record.product_id.id,
                    'name':record.description,
                    'product_uom_qty':record.qty,
                    'product_uom':record.product_uom.id,
                    'price_unit':record.product_id.lst_price
                    }
        return data
    
    @api.onchange('opportunity_id')
    def opportunity_id_change(self):
        if not self.opportunity_id:
            return {}
        if not self.partner_id:
            self.partner_id = self.opportunity_id.partner_id.id

        new_lines = self.env['sale.order.line']
        for line in self.opportunity_id.lead_product_ids:

            data = self._prepare_sale_order_lines_from_opportunity(line)
            new_line = new_lines.new(data)
            new_lines += new_line

        self.order_line += new_lines
        return {}
    

