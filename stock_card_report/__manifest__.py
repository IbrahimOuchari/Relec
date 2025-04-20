
{
    "name": "Rapport de Fiche de Stock",
    "summary": "Add stock card report on Inventory Reporting.",
    "version": "14",
    "category": "Warehouse",
    "author": "BMG Tech",
    "license": "AGPL-3",
    "depends": ["stock", "date_range", "report_xlsx_helper"],
    "data": [
        "security/ir.model.access.csv",
        "data/paper_format.xml",
        "data/report_data.xml",
        "reports/stock_card_report.xml",
        "wizard/stock_card_report_wizard_view.xml",
    ],
    "installable": True,
}
