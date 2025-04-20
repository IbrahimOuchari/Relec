{
    "name": "Module Z2S",
    "author": "BMG Tech",
    "version": "14",
    "summary": "Modification différents modules Z2S",

    "depends": [
        "base", "mail", "web", "hr", "contacts", "mrp", "cup_is_customer_is_vendor",
        "sale_isolated_quotation","stock", "mrp", "sale_isolated_quotation"

    ],

    "data": [
        "security/ir.model.access.csv",
        "views/bc_z2s_view.xml",
        "views/livraison.xml",
        #"wizards/select_of_picking.xml",
        "views/livraison_of.xml",
        "views/product_template.xml",
        "views/mrp_product_bom.xml",
        "views/invoice_view.xml",
        "views/mrp_routing_view.xml",
        "views/mrp_gamme_operation.xml",
        "views/hr.xml",
        'views/purchase.xml',

    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "AGPL-3",
}
