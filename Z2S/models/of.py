from odoo import api, fields, models
from datetime import date
from odoo.tools import float_compare
from odoo.tools import float_is_zero
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError



class livraison_OF(models.Model):
    _inherit = 'mrp.production'

    date_creation = fields.Date(string="Date Création OF", default=lambda self: date.today())
    date_realisation = fields.Date(string="Date Réalisation", compute='_compute_today_date', store=True, )

    def action_annule_of(self):
        for rec in self:
            rec.state = 'cancel'
            rec.state_of = 'cancel'

    @api.depends('state')
    def _compute_today_date(self):
        for record in self:
            if record.state == 'done':
                record.date_realisation = date.today()

    client_id = fields.Many2one('res.partner', string="Client", related="product_id.client_id")
    ref_product_client = fields.Char('product.template', related="product_id.ref_product_client")
    description = fields.Text('product.template', related="product_id.description_sale")
    sale_order_count = fields.Char()

    stock_move_line_ids = fields.One2many('stock.move.line', 'ref_of', string='Liste des livraison sur l\'of')

    quantite_livre = fields.Float("Quantité Totale livrée", compute="_compute_qte", digits='Product Unit of Measure',
                                  index=True, store=True)
    quantity_done = fields.Integer('stock_move_line_ids.qty_done')
    quantite_restante = fields.Float("Quantité Reste à livrer", compute="_compute_qte_restante",
                                     digits='Product Unit of Measure', index=True, store=True)

    @api.depends('stock_move_line_ids', 'quantity_done', 'quantite_livre')
    def _compute_qte(self):
        for record in self:
            total = 0
            for rec in record.stock_move_line_ids:
                if rec.ref_of.name == record.name:
                    total += rec.qty_done
            record.quantite_livre = total

    @api.depends('qty_producing', 'quantite_livre', 'quantite_restante')
    def _compute_qte_restante(self):
        for record in self:
            reste = record.qty_producing - record.quantite_livre
            record.quantite_restante = reste

    active_livraison = fields.Boolean(default=False, string="Livraison Complète",
                                      store=True, compute="_compute_livraison_total")

    @api.depends('stock_move_line_ids', 'quantite_restante', 'qty_producing', 'quantite_livre')
    def _compute_livraison_total(self):
        for compute in self:
            if compute.quantite_restante == 0 and compute.qty_producing != 0:
                compute.active_livraison = True
            else:
                compute.active_livraison = False

    state_of = fields.Selection([
        ('none', 'Non Livré'),
        ('livre', 'Livré'),
        ('cancel', 'Annulé'),
    ], string='State OF',
        compute='_compute_state_mrp', copy=False, index=True, readonly=True, store=True,
        tracking=True)

    @api.depends('active_livraison', 'quantity_done', 'quantite_livre', 'quantite_restante', 'qty_producing')
    def _compute_state_mrp(self):
        for production in self:
            if production.quantite_restante == 0 and production.qty_producing != 0:
                production.state_of = 'livre'
            else:
                production.state_of = 'none'


class StockPickingline(models.Model):
    _inherit = "stock.move"

    date_done_id = fields.Datetime(related="picking_id.date_done")
    num_bl = fields.Char(related="picking_id.name")
