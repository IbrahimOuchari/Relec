
from odoo import _, api, models
from odoo.exceptions import ValidationError


class StockQuant(models.Model):
    _inherit = "stock.quant"

    # Raise an error when trying to change a quant
    # which corresponding stock location is blocked
    @api.constrains("location_id")
    def check_location_blocked(self):
        for record in self:
            if record.location_id.block_stock_entrance:
                raise ValidationError(
                    _(
                        "L'emplacement %s est bloqué et ne peut "
                         "pas être utilisé pour déplacer le produit %s"
                    )
                    % (record.location_id.display_name, record.product_id.display_name)
                )
