from odoo.tools.float_utils import float_compare
from odoo import models, fields, _
from odoo.exceptions import UserError

class StockQuant(models.Model):
    _inherit = 'stock.quant'

    def _apply_inventory(self):
        move_vals = []
        if not self.user_has_groups('stock.group_stock_manager'):
            raise UserError(_('Only a stock manager can validate an inventory adjustment.'))

        for quant in self:
            if float_compare(quant.inventory_diff_quantity, 0, precision_rounding=quant.product_uom_id.rounding) != 0:
                if quant.location_id.usage == 'internal':
                    if quant.inventory_diff_quantity > 0:
                        move_vals.append(
                            quant._get_inventory_move_values(
                                quant.inventory_diff_quantity,
                                quant.product_id.with_company(quant.company_id).property_stock_inventory,
                                quant.location_id,
                                package_dest_id=quant.package_id
                            )
                        )
                    else:
                        move_vals.append(
                            quant._get_inventory_move_values(
                                -quant.inventory_diff_quantity,
                                quant.location_id,
                                quant.product_id.with_company(quant.company_id).property_stock_inventory,
                                package_id=quant.package_id
                            )
                        )
                else:
                    raise UserError(_('Inventory adjustments can only be applied to internal locations.'))

        # Create and validate the stock moves
        if move_vals:
            moves = self.env['stock.move'].with_context(inventory_mode=False).create(move_vals)
            moves._action_done()

        # Force recalculate `qty_available`
        for quant in self:
            quant.product_id._compute_quantities()

        # Update metadata and reset fields
        self.location_id.write({'last_inventory_date': fields.Date.today()})
        for quant in self:
            quant.inventory_date = fields.Date.today()
        self.write({'inventory_quantity': 0, 'inventory_diff_quantity': 0, 'user_id': False})
