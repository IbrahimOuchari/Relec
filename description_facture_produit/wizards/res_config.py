
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    group_use_product_description_per_inv_line = fields.Boolean(
        string="Autoriser l'utilisation uniquement de la description du produit sur les lignes de facture",
        implied_group="description_facture_produit."
        "group_use_product_description_per_inv_line",
        help="""Permet d'utiliser la description de l'article seulement dans la ligne de facture""",
    )
