
from odoo import fields, models


class CrmStage(models.Model):

    _inherit = "crm.stage"

    probability = fields.Float(
        "Probabilité (%)",
        required=True,
        default=10.0,
        help="Ce pourcentage représente la probabilité par défaut/moyenne au Cas pour que cette étape soit un succès ",
    )
    on_change = fields.Boolean(
        "Modifier la Probabilité Automatiquement",
        help="Le réglage de cette étape modifiera automatiquement la probabilité dans l'opportunité ",
    )

    _sql_constraints = [
        (
            "check_probability",
            "check(probability >= 0 and probability <= 100)",
            "The probability should be between 0% and 100%!",
        )
    ]
