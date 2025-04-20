# -*- coding: utf-8 -*-

{
    'name': 'Lignes de Commande Achat',
    'version': '14',
    'author': 'BMG Tech',
    'website': '',
    'category': 'Purchase',
    'description': """Enhancement in Purchase module""",
    'depends': ['base','purchase'],
    'license': 'LGPL-3',
    'data': [
        'views/purchase_order_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
