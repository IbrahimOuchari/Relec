
{
    'name': "Panneau de Recherche Catégorie",
    'author': "BMG Tech",
    'website': '',
    'version': '14',
    'category': 'Extra Tools',
    'license': 'OPL-1',
    'images': ['static/description/main_banner.png'],
   
    
    'summary': """Enable search panel hide & show by a toggle button.""",
    'description': """Search panel hide & show
     
     List view search panel hide
     Kanban view search panel hide
    Colum Width,
    Page Size,
    Advance Dynamic Tree View ,
	Advance Search ,
	Best List View Apps ,
	Best Tree View Apps ,
    Dynamic List View,
    Dynamic List ,
    Dynamic Search ,
    Dynamic Column ,
	Dynamic List View Apps , 
	Drag and edit columns ,
    List View ,
    List View Manage ,
    List View Management ,
    List View Column ,
	List view Advance Search ,
	List View Apps ,
	List View Management Apps ,
	Listview ,
    Field Display Control ,
    Field Hide Show ,
	Freeze List View Header ,    
	Hide/Show list view columns ,
	Odoo List View ,
	Odoo Advanced Search ,
	Odoo Manage List View ,
	Tree View Apps ,    
	Tree/List View Apps  ,
	Tree view Advance Search ,
	Treeview ,
	Tree View ,     
     
    """,


    # any module necessary for this one to work correctly
    'depends': ['web', 'product'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/web_views.xml',
        'views/product_search_view.xml',
    ],
    # only loaded in demonstration mode
     
    'qweb': ['static/src/xml/*.xml']
}
