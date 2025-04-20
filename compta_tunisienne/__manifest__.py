# -*- coding: utf-8 -*-
{
    'name': 'Comptabilité Tunisienne',
    'version': '14',
    'author': 'BMG Tech',
    'website': '',
    'summary': 'Template du plan comptable Tunisien',
    'category': 'Localization/Account Charts',
    'description': """
      Il s'agit du module de base pour gérer le modèle de plan comptable et fiscal pour les entreprises en Tunisie.
       Ce module charge le modèle du plan de comptes standard tunisien et permet de générer les états
       comptables aux normes tunisiennes.""",
    'depends': ['base_iban', 'account'],
    'init_xml': [],
    'data': [
        'data/tn_pcg_taxes.xml',
        'data/plan_comptable_general.xml',
        'data/tn_tax.xml',
        'data/tn_fiscal_templates.xml',
        #add on migration
        'data/account_chart_template.xml',
        # 'data/account_chart_template.yml',
        
    ],
    'images': [
        'images/wct_tn.png',
    ],
    'test': [],
    'demo_xml': [],
    # 'active': True,
    'installable': True,
}
