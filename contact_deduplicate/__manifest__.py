# -*- coding: utf-8 -*-
{
    'name': "Contact Bloquer Doublons",
    'summary': """Contact: Deduplicate module""",
    'description': """Contact: Deduplicate module""",
    'author': 'BMG Tech',
    'maintainer': '',
    'website': "",
    'category': 'Contacts',
    'version': '13.0.0.0.0',
    'depends': ['base', 'contacts'],
    'data': [
        'data/ir_cron_data.xml',
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml'
    ],
    'images': ['static/description/banner.png'],
    'post_init_hook': '_initial_setup',
    'license': "AGPL-3",
    'installable': True,
    'application': False,
}
