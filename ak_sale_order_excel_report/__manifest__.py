
{
    'name': "Télécherger BC Excel",
    'author': 'BMG Tech',
    'website': "",
    'summary': """Print sale excel report SO action""",
    'description': """This module will print excel report of sale.""",
    'license': 'AGPL-3',
    'category': 'Sales',
    'version': '14',
    'depends': [
        'sale_management',
    ],
    'data': [
        'report/menu_sale_xlsx.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
