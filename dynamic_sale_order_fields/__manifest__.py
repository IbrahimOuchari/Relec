
{
    'name': 'Ajout Champ Personnalisé SO',
    'version': '14',
    'summary': """Ability To Add Custom Fields in Sale Order From User Level""",
    'description': """Ability To Add Custom Fields in Sale Order From User Level,Sale Order Custom Fields,
                      Sale Order Dynamic Fields, odoo13, Dynamic Sale Order Fields, Dynamic Fields, Create Dynamic Fields, Community odoo Studio""",
    'category': 'Sales',
    'author': 'BMG Tech',
    'depends': ['sale_management'],
    'data': [
        'data/widget_data.xml',
        'security/ir.model.access.csv',
        'security/sale_dynamic_security_group.xml',
        'wizard/sale_order_fields.xml',
        'views/sale_order_view.xml',
        'views/ir_fields_search_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
