
{
    'name': "Masquer Coût et Prix Produit",
    'author': 'BMG Tech',
    'category': 'Sales',
    'summary': """Masquer le prix de vente et de revient du produit pour activer l'affichage donner le droit d'accès à l'utilisateur""",
    'website': '',
    'description': """Masquer le prix de vente et de revient du produit pour activer l'affichage donner le droit d'accès à l'utilisateur""",
    'version': '14',
    'depends': ['base','sale_management','product'],
    'data': ['security/show_sale_cost_price_fields.xml','views/view_sale_cost_price_product.xml'
           ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',    
    'installable': True,
    'application': True,
    'auto_install': False,
}
