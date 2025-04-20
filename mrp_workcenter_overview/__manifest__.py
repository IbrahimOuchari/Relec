
{
    'name': 'Tableau de Bord Poste',
    'summary': 'MRP Workcenter Overview',
    'version': '14',
    'category': 'Manufacturing/Manufacturing',
    'summary': """
MRP Workcenter Overview backport 
""",
    'author': "BMG Tech",
    'website': '',
    'license': 'LGPL-3',
    'images': ['images/screen.png'],
    'depends': [
	'mrp',
    ],
    'data': [
        'views/mrp_workcenter_views.xml',
    ],
    'installable': True,
    'application': False,
}
