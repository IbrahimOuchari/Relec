# -*- encoding: utf-8 -*-
{
	"name": "Ajout Produit CRM",
	"version": "14",
	"author": "BMG Tech",
	"website": "",
	"sequence": 5,
	"depends": [
		"base",'sale_crm','sale','product'
	],
	"category": "Settings",
	"complexity": "easy",
	"description": """
	Ce module permet d'ajouter des produits sur opportunité et de créer un devis avec cela. 
	""",
	"data": [
		'security/ir.model.access.csv',
		'views/opportunity_product.xml',
	],
	"demo": [
	],
	"test": [
	],
	"auto_install": False,
	"installable": True,
	"application": True,
    'images': ['static/description/banner.png'],
	'license': 'LGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
