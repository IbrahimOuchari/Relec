
{
    'name': 'Rapports Comptables PDF',
    'version': '14',
    'category': 'Invoicing Management',
    'summary': 'Rapports comptables PDF',
    'sequence': '10',
    'author': 'BMG Tech',
    'license': 'LGPL-3',
    'website': '',
    'depends': ['account'],
    'live_test_url': '',
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/account_pdf_reports.xml',
        'views/account_reports_settings.xml',
        'wizards/partner_ledger.xml',
        'wizards/general_ledger.xml',
        'wizards/trial_balance.xml',
        'wizards/balance_sheet.xml',
        'wizards/profit_and_loss.xml',
        'wizards/tax_report.xml',
        'wizards/aged_partner.xml',
        'wizards/journal_audit.xml',
        'reports/report.xml',
        'reports/report_partner_ledger.xml',
        'reports/report_general_ledger.xml',
        'reports/report_trial_balance.xml',
        'reports/report_financial.xml',
        'reports/report_tax.xml',
        'reports/report_aged_partner.xml',
        'reports/report_journal_audit.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
    'qweb': [],
}
