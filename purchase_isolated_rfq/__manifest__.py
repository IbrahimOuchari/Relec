
{
    "name": "Isoler RFQ du BC Achat",
    "version": "14",
    "author": "BMG Tech",
    "category": "Purchases",
    "website": "",
    "depends": ["purchase"],
    "license": "AGPL-3",
    "data": ["data/ir_sequence_data.xml", "views/purchase_views.xml"],
    "maintainers": ["kittiu"],
    "installable": True,
    "uninstall_hook": "uninstall_hook",
    "post_init_hook": "post_init_hook",
}
