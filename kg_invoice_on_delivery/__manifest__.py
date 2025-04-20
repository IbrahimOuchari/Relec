
{
    'name': "Facturation BL",

    'summary': """
        ajoute bouton facturation dans stock picking""",

    'description': """
        Option for invoice generation from delivery
    """,

    'author': "BMG Tech",
    'maintainer': "",
    'website': "",

    'category': 'Accounting',
    'version': '14',
    'license': 'AGPL-3',

    'depends': ['base','stock','sale','sale_stock'],
    'images': ["static/description/banner.png"],

    'data': [
        'views/validate.xml',
    ],
}
