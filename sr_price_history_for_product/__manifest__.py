{
    'name': "Historique Prix Produit Achat et Vente",
    'version': '14',
    'summary': "With the help of this module, You can find the rate which you have given to that customers/suppliers in past for that product.",
    'category': 'Sales',
    'description': """
    purchase price history
    sale price history
    easy to find previous cost price
    easy to find previous sale price
    price history
    purchase cost history
    inherit product
    track the price in product template
    track the price in product variant
    product wise sale price history
    product wise purchase price history
    product wise sale history
    
    """,
    'author': "BMG Tech",
    'depends': ['base', 'sale_management', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/inherited_product.xml',
        'views/inherited_res_config_setting.xml',
    ],
    'demo': [],
    "external_dependencies": {},
    "license": "OPL-1",
    'installable': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],

}
