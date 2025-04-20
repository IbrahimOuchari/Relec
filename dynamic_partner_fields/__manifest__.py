
{
    'name': 'Ajout Champ Personnalisé Contact',
    'version': '14',
    'summary': """Ability To Add Custom Fields in Partner From User Level""",
    'description': """Ability To Add Custom Fields in Partner From User Level,Partner Custom Fields,
                      Partner Dynamic Fields, odoo13, Dynamic Partner Fields, Dynamic Fields, Create Dynamic Fields, Community odoo Studio""",
    'category': 'Extra Tools',
    'author': 'BMG Tech',
    'depends': ['contacts'],
    'data': [
        'data/widget_data.xml',
        'security/ir.model.access.csv',
        'security/partner_security_group.xml',
        'wizard/partner_fields_view.xml',
        'views/partner_form_view.xml',
        'views/ir_fields_search_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
