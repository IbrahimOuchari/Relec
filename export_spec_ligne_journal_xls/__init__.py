from . import models

try:
    from . import report
except ImportError:
    import logging

    logging.getLogger("odoo.module").warning(
        """report_xlsx_helper not available in addons path.
    export_spec_ligne_journal_xls will not be usable"""
    )
