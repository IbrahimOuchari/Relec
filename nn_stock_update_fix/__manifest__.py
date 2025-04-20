{
    'name': 'Fix Stock Inventory Adjustment Issue',
    'version': '1.0',
    'summary': 'Fixes stock inventory adjustment behavior in Odoo 14',
    'description': """
        This module customizes the stock inventory adjustment logic to:
        - Prevent redundant inventory adjustment quants.
        - Ensure stock updates are correctly reflected in the "On Hand" quantity.
    """,
    'author': 'Your Name',
    'depends': ['stock'],
    'data': [],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
