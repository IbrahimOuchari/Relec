
{
    'name': "Montant dû dans la vue contact",
    'author': 'BMG Tech',
    'category': 'Accounting/Accounting',
    'summary': """Afficher le montant dû du client ou fournisseur dans la vue contact""",
    'website': '',
    'company': '',
    'maintainer': '',
    'description': """Afficher le montant dû du client ou fournisseur dans la vue contact""",
    'version': '1.0',
    'depends': ['base', 'sale', 'account', 'purchase'],
    'data': [
               "views/res_partner_view.xml",
            ],
    "images":  ['static/description/Banner.gif'],
    "qweb":  [],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
