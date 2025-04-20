
{
    'name': 'Figer Colonne Tableau Pivot',
    'version': '14',
    'summary': 'Helps to stick the pivot view (Row and Column)',
    'description': 'Helps to stick the pivot view (Row and Column)',
    'category': 'Tools',
    'author': "BMG Tech",
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'web'],
    'qweb': [
        'static/src/xml/pivot.xml',
    ],
    'data': [
        'views/assets.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
