from odoo import models, api, fields
import logging

_logger = logging.getLogger(__name__)


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # Store the picking directly on the move line
    picking_id = fields.Many2one(
        comodel_name="stock.picking",
        string="Related Picking",
        compute="_compute_picking_id",
        store=True,
    )

    # Get the BL number directly from the related picking
    num_bl = fields.Char(
        string='BL Number',
        related='picking_id.name',
        store=True,
    )

    @api.depends("move_line_ids", "move_line_ids.picking_id")
    def _compute_picking_id(self):
        for line in self:
            picking = line.mapped("move_line_ids.picking_id")
            line.picking_id = picking and picking[0] or False
            _logger.info(
                f"Computed picking_id for move line {line.id}: {line.picking_id.name if line.picking_id else 'None'}")


class AccountMove(models.Model):
    _inherit = "account.move"

    # Keep this for backward compatibility if needed
    picking_ids = fields.Many2many(
        comodel_name="stock.picking",
        string="Related Pickings",
        store=True,
        compute="_compute_picking_ids",
        help="Related pickings "
             "(only when the invoice has been generated from a sale order).",
    )

    # This field will now show all BL numbers joined together
    bl_numbers = fields.Char(
        string="BL Numbers",
        compute="_compute_bl_numbers",
        store=True,
    )

    @api.depends("invoice_line_ids", "invoice_line_ids.move_line_ids")
    def _compute_picking_ids(self):
        for invoice in self:
            _logger.info(f"Computing picking_ids for invoice {invoice.id}")
            picking_ids = invoice.mapped("invoice_line_ids.move_line_ids.picking_id")
            _logger.info(f"Mapped picking_ids: {picking_ids}")
            invoice.picking_ids = picking_ids
            _logger.info(f"Computed picking_ids for invoice {invoice.id}: {invoice.picking_ids}")

    @api.depends("picking_ids")
    def _compute_bl_numbers(self):
        for invoice in self:
            bl_values = invoice.picking_ids.mapped('name')
            invoice.bl_numbers = ', '.join(bl_values) if bl_values else False
            _logger.info(f"BL numbers for invoice {invoice.id}: {invoice.bl_numbers}")