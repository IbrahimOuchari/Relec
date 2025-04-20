
from odoo import fields, models


class CrmTeam(models.Model):
    _inherit = "crm.team"

    manual_delivery = fields.Boolean(
        string="Livraison Manuelle",
        help="Si activé, les livraisons ne sont pas créées lors de la confirmation du SO. "
         "Vous devez utiliser le bouton Créer une livraison pour réserver et "
         "expédier la marchandise.",
        default=True,
    )
