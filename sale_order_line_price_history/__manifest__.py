
{
    "name": "Historique Prix BC Vente",
    "version": "14",
    "category": "Sales Management",
    "author": "BMG Tech",
    "website": "",
    "license": "AGPL-3",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "wizards/sale_order_line_price_history.xml",
        "views/sale_views.xml",
        "views/assets.xml",
    ],
    "qweb": ["static/src/xml/sale_line_price_history_widget.xml"],
    "installable": True,
}
