
from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = "product.category"

    allow_negative_stock = fields.Boolean(
        string="Autoriser le stock négatif",
        help="Autoriser les niveaux de stock négatifs pour les produits stockables "
        "rattaché à cette catégorie. Les options ne s'appliquent pas aux produits "
        "attachés aux sous-catégories de cette catégorie.",
    )


class ProductTemplate(models.Model):
    _inherit = "product.template"

    allow_negative_stock = fields.Boolean(
        string="Autoriser le stock négatif",
        help="Si cette option n'est pas active sur ce produit ni sur son "
        "catégorie de produit et que ce produit est un produit stockable, "
        "alors la validation des mouvements de stock liés sera bloquée si "
        "le niveau de stock devient négatif avec le mouvement de stock.",
    )
