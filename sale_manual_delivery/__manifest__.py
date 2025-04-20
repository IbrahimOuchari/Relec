{
    "name": "Livraison Manuelle des BC Vente",
    "category": "Sale",
    "author": "BMG Tech",
    "license": "AGPL-3",
    "version": "14",
    "summary": "Créer les BL manuellement depuis les BC",
    "depends": ["delivery", "sale_stock", "sales_team", "sale", "Z2S", "sale_order_line_menu"

                ],
    "data": [
        "security/ir.model.access.csv",
        "views/crm_team.xml",
        "views/sale_order.xml",
        "wizard/manual_delivery.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
