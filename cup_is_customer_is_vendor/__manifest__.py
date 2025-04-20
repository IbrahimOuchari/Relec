# -*- coding: utf-8 -*-
{
    'name': "Identification Partenaire",

    'summary': """
        Est un client est un fournisseur dans la vue contact
""",

    'description': """
      
    """,

    'license': "LGPL-3",
    'images': ['static/description/cupdev2.png'],
    'author': 'BMG Tech',
    'website': "",

    # Categories can be used to filter modules in modules listing
    
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account','sale_management','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}