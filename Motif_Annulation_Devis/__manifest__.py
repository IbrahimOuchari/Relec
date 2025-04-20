{
    'name': "Motif d'Annulation de Devis",
    'author': 'BMG Tech',
    'category': 'Sales',
    'summary': """Motif d'Annulation de Devis""",
    'license': 'AGPL-3',
    'website': '',
    'description': """""",
    'version': '14.0.1.0',
    'depends': ['base','sale_management','sales_team'],
    'data': ['security/ir.model.access.csv','wizard/add_sale_cancel_reason_view.xml','views/quotation_cancel_reason.xml','views/sale_order_view.xml'
           ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
