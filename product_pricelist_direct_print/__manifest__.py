
{
    "name": "Imprimer Liste des Prix Produits",
    "summary": "Imprimer la liste de prix à partir de l'option de menu, des modèles de produits, des variantes de produits ou des listes de prix",
    "version": "14",
    "category": "Product",
    "author": "BMG Tech",
    "license": "AGPL-3",
    "depends": ["sale"],
    "data": [
        "security/ir.model.access.csv",
        "views/report_product_pricelist.xml",
        # 'mail_template_data' has to be after 'report_product_pricelist'
        "data/mail_template_data.xml",
        "wizards/product_pricelist_print_view.xml",
    ],
}
