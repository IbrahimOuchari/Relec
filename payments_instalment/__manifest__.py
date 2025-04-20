# -*- coding: utf-8 -*-
{
    'name': 'Paiement a Terme Facture',
    'version': '1.0',
    'category': 'Installments Notifications',
    'summary': ' installments and notifications Management',
    'sequence': '5',
    'author': 'BMG Tech',
    'depends': ['account'],
    'data': [
        # 'security/groups.xml',
        'security/ir.model.access.csv',
        'views/payments.xml',
        'data/crons.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
