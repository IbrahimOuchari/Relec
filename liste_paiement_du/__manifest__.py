
{
    "name": "Liste des paiements dus",
    "version": "14",
    "category": "Generic Modules/Payment",
    "development_status": "Beta",
    "author": "BMG Tech",
    "summary": "Ce module ajoute une liste d'échéances des paiements en attente. La liste contient tous les paiements attendus, générés par les factures. La liste est entièrement filtrable.",
    "website": "",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": ["views/payment_view.xml"],
    "pre_init_hook": "pre_init_hook",
    "installable": True,
    "auto_install": False,
}
