{
    'name': 'Montant Payé Liste des Factures',
    'version': '14',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'author': 'BMG Tech',
    'depends': ['base', 'mail', 'account',
                ],
    'images': ['images/icon.png'],
    'data': [
             'views/account_invoice_view.xml',
             ],
    'installable': True,
    'application': True,
}
