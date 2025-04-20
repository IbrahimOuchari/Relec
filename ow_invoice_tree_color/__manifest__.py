
{
    'name': 'Couleur Ligne Facture Selon Status Paiement',
    'summary': 'Invoice Treeview state color',
    'version': '14',
    'category': 'Accounting',
    'summary': """
Show colors on Invoice Treeview depending on state.
""",
    'author': "BMG Tech",
    'website': '',
    'license': 'LGPL-3',
    'images': ['images/screen.png'],
    'depends': [
	'account',
    ],
    'data': [
        'views/invoice_tree.xml',
    ],
    'installable': True,
    'application': False,
}
