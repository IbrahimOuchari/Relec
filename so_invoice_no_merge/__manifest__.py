# -*- coding: utf-8 -*-
{
    'name': "Choix Fusion Facture de BC",

    'summary': """
        Choose whether to merge multiple sale orders into one invoice or invoice them separately
        """,

    'description': """
        This module grants the user the choice to whether consolidate multiple sales orders in one invoice 
        or note when selecting them in the Orders To Invoice page.

    """,
    'author': "BMG Tech",
    'category': 'Accounting',
    'version': '14',
    'depends': ['base', 'sale'],
    'data': [
        'wizard/wizard.xml',
    ],
    'images':  ["static/description/image.png"],

}
