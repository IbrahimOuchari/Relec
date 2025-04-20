from odoo import _, api, fields, models
from odoo.exceptions import UserError
from odoo.tools import float_compare


class ManualDeliveryLine(models.TransientModel):
    _name = "manual.delivery.line"
    _description = "Manual Delivery Line"

    manual_delivery_id = fields.Many2one(
        "manual.delivery",
        string="Wizard",
        ondelete="cascade",
        required=True,
        readonly=True,
    )
    order_line_id = fields.Many2one(
        "sale.order.line",
        string="Lignes de Vente",
        required=True,
        readonly=True,
        ondelete="cascade",
    )
    product_id = fields.Many2one(related="order_line_id.product_id")
    name = fields.Text(related="order_line_id.name")
    qty_ordered = fields.Float(
        string="Commandée",
        related="order_line_id.product_uom_qty",
        help="Quantité commandée dans le bon de commande associé",
        readonly=True,
    )
    qty_procured = fields.Float(related="order_line_id.qty_procured")
    quantity = fields.Float()

    @api.constrains("quantity")
    def _check_quantity(self):
        """ Prevent delivering more than the ordered quantity """
        if any(
                float_compare(
                    line.quantity,
                    line.qty_ordered - line.qty_procured,
                    precision_rounding=line.product_id.uom_id.rounding,
                )
                > 0.00
                for line in self
        ):
            raise UserError(
                _(
                    "Vous ne pouvez pas livrer plus que la quantité restante. "
                    "Si vous devez le faire, veuillez d'abord modifier le bon de commande."
                )
            )

    poste_id = fields.Char(readonly=True, related="order_line_id.poste", store=True)
    qty_dispo = fields.Float(readonly=True, related="product_id.qty_available")

    @api.constrains("quantity")
    def _check_quantity_available(self):
        """ Prevent delivering more than the quantity on hand """
        if any(
                float_compare(
                    line.quantity,
                    line.qty_dispo,
                    precision_rounding=line.product_id.uom_id.rounding,
                )
                > 0.00
                for line in self
        ):
            raise UserError(
                _(
                    "Stock indisponible. Veuillez vérifier la quantité"
                )
            )
