
{
    "name":  "Stockage Document Contact",
    "summary":  "Stocker des documents dans contact",
    "category":  "Document",
    "version":  "14",
    "sequence":  1,
    "author":  "BMG Tech",
    "license": 'OPL-1',
    "images": ['static/description/Banner.png'],
    "depends":  ['base','hr'],
    'data': [
                'security/ir.model.access.csv',
                'views/document_view.xml',
                'views/res_partner_view.xml',
                'views/hr_employee_view.xml',
                'views/menu.xml',
            ],
    "application":  True,
    "installable":  True,
    "auto_install":  False,
}
