{
    "name"          : "Rapport de Stock",
    "version"       : "14",
    "author"        : "BMG Tech",
    "website"       : "",
    "category"      : "Reporting",
    "license"       : "LGPL-3",
    "support"       : "",
    "summary"       : "Télécharger rapport de stock en Excel",
    "description"   : """
        Télécharger rapport de stock en Excel
    """,
    "depends"       : [
        "product",
        "stock",
    ],
    "data"          : [
        "wizard/ms_report_stock_wizard.xml",
        "security/ir.model.access.csv",
    ],
    "demo"          : [],
    "test"          : [],
    "images"        : [
        "static/description/images/main_screenshot.png",
    ],
    "qweb"          : [],
    "css"           : [],
    "application"   : True,
    "installable"   : True,
    "auto_install"  : False,
}