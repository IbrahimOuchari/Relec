# Copyright 2017-2020 ForgeFlow S.L.
#   (http://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    discrepancy_threshold = fields.Float(
        string="Seuil de taux d'écart maximum",
        digits=(3, 2),
        help="MTaux d'écart maximal autorisé pour tout produit lors d'un "
         "ajustement d'inventaire",
    )
