{
    'name': "Liste des Produits Top Vente",
    'author': 'BMG Tech',
    'category': 'Sales',
    'summary': """Afficher la liste des produits les plus vendus""",
    'website': '',
    'license': 'AGPL-3',
    'description': """ """,
    'version': '14',
    'depends': ['base','sale_management'],
    'data': ['security/ir.model.access.csv','wizard/menu_top_selling_product_view.xml','views/menu_sales_view.xml','views/top_selling_products_view.xml','views/top_selling_quantity_view.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}




