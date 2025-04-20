# -*- coding: utf-8 -*-
{
    'name': 'Rapport Produits par Fournisseur',
    'summary':"""Ce module affiche une liste récapitulant les achats de chaque fournisseur par produit""",
    'depends': ['product','purchase','stock'],
    'version': '14',
    'author':'BMG Tech',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/porduct_supplier_view.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
}
