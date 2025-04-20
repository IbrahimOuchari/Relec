# Copyright 2017-2020 ForgeFlow S.L.
#   (http://www.forgeflow.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class StockLocation(models.Model):
    _inherit = "stock.location"

    discrepancy_threshold = fields.Float(
        string="Seuil de taux d'écart maximum",
        digits=(3, 2),
        help="Taux d'écart maximum autorisé pour tout produit lors de l'exécution d'un ajustement des stocks. Les seuils définis dans les emplacements ont "
         "les mêmes préférence sur ceux de Warehouse.",
    )
    propagate_discrepancy_threshold = fields.Boolean(
        string="Seuil d'écart de propagation",
        help="Propager le seuil de taux de divergence maximal aux emplacements enfants",
    )

    def write(self, values):
        res = super().write(values)
        # Set the discrepancy threshold for all child locations
        if values.get("discrepancy_threshold", False):
            for location in self.filtered(
                lambda loc: loc.propagate_discrepancy_threshold and loc.child_ids
            ):
                location.child_ids.write(
                    {
                        "discrepancy_threshold": values["discrepancy_threshold"],
                        "propagate_discrepancy_threshold": True,
                    }
                )
        return res
