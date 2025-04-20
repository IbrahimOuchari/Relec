
{
    'name': 'Ajout Champ Personnalisé Produit',
    'version': '14',
    'summary': """Ability To Add Custom Fields in Products From User Level""",
    'description': """Ability To Add Custom Fields in Products From User Level,Product Custom Fields,
                      Product Dynamic Fields, odoo13, Dynamic Product Fields, Dynamic Fields, Create Dynamic Fields, Community odoo Studio""",
    'category': 'Sales',
    'author': 'BMG Tech',
    'depends': ['product'],
    'data': [
        'data/widget_data.xml',
        'security/ir.model.access.csv',
        'security/product_security_group.xml',
        'wizard/product_fields_view.xml',
        'views/product_form_view.xml',
        'views/ir_fields_search_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
