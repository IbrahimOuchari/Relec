from odoo import api, fields, models, tools


class MrpRoutingWorkcenter(models.Model):
    _name = 'mrp.routing.operation'
    _description = 'Work Center Usage'
    _order = 'sequence, id'
    _check_company_auto = True

    name = fields.Char('Operation', required=True)
    workcenter_id = fields.Many2one('mrp.workcenter', 'Work Center', required=True, check_company=True)
    sequence = fields.Integer(
        'Sequence', default=100,
        help="Gives the sequence order when displaying a list of routing Work Centers.")
    routing_id = fields.Many2one(
        'mrp.routing', 'Gamme',
        index=True, ondelete='cascade')
    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.company)
    worksheet_type = fields.Selection([
        ('pdf', 'PDF'), ('google_slide', 'Google Slide'), ('text', 'Text')],
        string="Work Sheet", default="text",
        help="Defines if you want to use a PDF or a Google Slide as work sheet."
    )
    note = fields.Text('Description', help="Text worksheet description")
    worksheet = fields.Binary('PDF')
    worksheet_google_slide = fields.Char('Google Slide', help="Paste the url of your Google Slide. Make sure the access to the document is public.")
    time_mode = fields.Selection([
        ('auto', 'Calculez sur base du temps compté'),
        ('manual', 'ixer la durée manuellement')], string='Duration Computation',
        default='manual')
    time_mode_batch = fields.Integer('Based on', default=10)
    time_cycle_manual = fields.Float(
        'Manual Duration', default=60,
        help="Time in minutes:"
        "- In manual mode, time used"
        "- In automatic mode, supposed first time when there aren't any work orders yet")
    time_cycle = fields.Float('Duration', compute="_compute_time_cycle")
    workorder_count = fields.Integer("# Work Orders", compute="_compute_workorder_count")
    workorder_ids = fields.One2many('mrp.workorder', 'operation_id', string="Work Orders")

    @api.depends('time_cycle_manual', 'time_mode', 'workorder_ids')
    def _compute_time_cycle(self):
        manual_ops = self.filtered(lambda operation: operation.time_mode == 'manual')
        for operation in manual_ops:
            operation.time_cycle = operation.time_cycle_manual
        for operation in self - manual_ops:
            data = self.env['mrp.workorder'].search([
                ('operation_id', '=', operation.id),
                ('qty_produced', '>', 0),
                ('state', '=', 'done')],
                limit=operation.time_mode_batch,
                order="date_finished desc")
            # To compute the time_cycle, we can take the total duration of previous operations
            # but for the quantity, we will take in consideration the qty_produced like if the capacity was 1.
            # So producing 50 in 00:10 with capacity 2, for the time_cycle, we assume it is 25 in 00:10
            # When recomputing the expected duration, the capacity is used again to divide the qty to produce
            # so that if we need 50 with capacity 2, it will compute the expected of 25 which is 00:10
            total_duration = 0  # Can be 0 since it's not an invalid duration for BoM
            cycle_number = 0  # Never 0 unless infinite item['workcenter_id'].capacity
            for item in data:
                total_duration += item['duration']
                cycle_number += tools.float_round((item['qty_produced'] / item['workcenter_id'].capacity or 1.0), precision_digits=0, rounding_method='UP')
            if cycle_number:
                operation.time_cycle = total_duration / cycle_number
            else:
                operation.time_cycle = operation.time_cycle_manual

    def _compute_workorder_count(self):
        data = self.env['mrp.workorder'].read_group([
            ('operation_id', 'in', self.ids),
            ('state', '=', 'done')], ['operation_id'], ['operation_id'])
        count_data = dict((item['operation_id'][0], item['operation_id_count']) for item in data)
        for operation in self:
            operation.workorder_count = count_data.get(operation.id, 0)

    def _get_comparison_values(self):
        if not self:
            return False
        self.ensure_one()
        return tuple(self[key] for key in  ('name', 'workcenter_id', 'time_mode', 'time_cycle_manual'))
