# -*- encoding: utf-8 -*-
{
    'name' : 'Coût Moyen Actuel',
    'version' : '14',
    'category'  : 'Warehouse',
    'summary': """Affiche le Coût Moyen Actuel dans le produit.""",
    'author' : 'BMG Tech',
    'website' : '',
    'license':  "",
    'depends' : ['product','stock','stock_account'],
    'data' : [
            'view/product.xml'
                ],
    "images":  ['static/description/image.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
