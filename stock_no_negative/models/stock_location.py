# ?? 2018 ForgeFlow (https://www.forgeflow.com)
# @author Jordi Ballester <jordi.ballester@forgeflow.com.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockLocation(models.Model):
    _inherit = "stock.location"

    allow_negative_stock = fields.Boolean(
        string="Autoriser le stock négatif",
        help="Autoriser les niveaux de stock négatifs pour les produits stockables "
        "attached to this location.",
    )
