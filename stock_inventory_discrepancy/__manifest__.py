
{
    "name": "Écart d'Inventaire des Stocks",
    "summary": "Adds the capability to show the discrepancy of every line in "
    "an inventory and to block the inventory validation when the "
    "discrepancy is over a user defined threshold.",
    "version": "14",
    "author": "BMG Tech",
    "website": "",
    "category": "Warehouse",
    "depends": ["stock"],
    "data": [
        "security/stock_inventory_discrepancy_security.xml",
        "views/assets_backend.xml",
        "views/stock_inventory_view.xml",
        "views/stock_warehouse_view.xml",
        "views/stock_location_view.xml",
    ],
    "license": "AGPL-3",
    "post_load": "post_load_hook",
    "installable": True,
    "application": False,
}
