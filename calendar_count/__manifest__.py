
{
    'name': 'Compteur calendrier par jour',
    'summary': """Compteur par jour calendrier""",
    'author': 'BMG Tech',
    "website": "",
    'category': "Extra Tools",
    'version': '14',
    # any module necessary for this one to work correctly
    'depends': ['web'],
    "license": "LGPL-3",

    'data': [
        'views/assets.xml',
        # 'views/res_config_settings_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml', ],
    'installable': True,
    'application': True,
    # If it's True, the modules will be auto-installed when all dependencies
    # are installed
    'auto_install': False,
}
