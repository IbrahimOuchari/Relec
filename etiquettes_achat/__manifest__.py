
{
    'name': "Etiquettes BC Achat",
    'author': 'BMG Tech',
    'category': 'Purchases',
    'summary': """Afficher les étiquettes de bon de commande dans les factures fournisseur""",
    'license': 'AGPL-3',
    'website': '',
    'description': """
""",
    'version': '14',
    'depends': ['base','purchase'],
    'data': ['security/ir.model.access.csv','views/purchase_tag_view.xml','views/purchase_tag_purchase_order_view.xml','views/purchase_tag_vendors_bill_view.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
