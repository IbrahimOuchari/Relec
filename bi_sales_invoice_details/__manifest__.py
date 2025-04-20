
{
	'name'			: 'Détails de la facture sur la commande client',
	'version'		: '14',
	'category'		: 'Sales',
	'author'		: 'BMG Tech',
	'summary'		: 'Afficher le montant facturé, le montant de la facture due, le montant de la facture payée dans le bon de commande',
	'description'	: """Afficher le montant facturé, le montant de la facture due, le montant de la facture payée dans le bon de commande	""",
	'website'		: '',
	'depends'		: ['base','sale','sale_management','stock'],
	'data'			: [
	                    'views/sales_invoice_views.xml'
						],
	'installable'	: True,
	'auto_install'	: False,
	"images":['static/description/Banner.png'],
}
