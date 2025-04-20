# -*- coding: utf-8 -*-
{
    'name': "Document Source Facture",
    'summary': """
         Ajoute un bouton dans la facture pour rederiger vers le document source
.
         """,
    'description': """
       Un bouton intelligent pour lier directement toutes vos factures et factures de fournisseurs avec leurs bons de commande et bons de commande associés et y accéder. 
    """,
    'author': 'BMG Tech',
    'website': "",
    'category': 'Accounting',
    'version': '14',
    'depends': ['base','account','purchase','sale'],
    'data': [
        'views/account_invoice_views.xml',
    ],
    "images":  ['static/description/Image.png'],
}
