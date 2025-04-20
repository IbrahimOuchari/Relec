{
    "name": "Réception Manuelle sur les BC Achat",
    "summary": """
        Empêche la génération automatique des prélèvements lors de la confirmation du bon de commande
         et ajoute la possibilité de les générer manuellement lorsque le fournisseur confirme
         les différentes lignes de commande.
    """,
    "version": "14",
    "license": "AGPL-3",
    "author": "BMG Tech",
    "depends": ["purchase_stock"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/create_manual_stock_picking.xml",
        "views/purchase_order_views.xml",
        "views/res_config_view.xml",
    ],
}
