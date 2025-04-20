# -*- coding: utf-8 -*-
{
    'name': "Traçabilité Produit User",
    'summary': "Ce module permet de connaître l'utilisateur qui a effectué un déplacement sur un produit",
    'description': """
        Ce module permet de connaître l'utilisateur qui a effectué un déplacement sur un produit    """,
    'author': 'BMG Tech',
    'website': "",
    'category': 'Inventory',
    'version': '14',
    "license": "LGPL-3",
    'depends': ['stock'],
    'data': ['views/stock_move_line_inherit.xml'],
    'images': ['static/description/icon.png'],
    "installable": True,
    "application": True,
    "auto_install": False,
}
