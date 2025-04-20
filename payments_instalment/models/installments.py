# -*- coding: utf-8 -*-


from datetime import date
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class AccountPaymentInherit(models.TransientModel):
    _inherit = 'account.payment.register'

    bill = fields.Many2one(
        'account.move',
    )

    notification_bill = fields.Many2one(
        'account.notification',
    )
    payment_mode = fields.Selection(
        selection=[('change', 'Espèce'), ('cheque', 'Chèque'), ('vir', 'Virement'), ('traite', 'Traite')])
    num = fields.Char()
    num_ch = fields.Char(string="Numéro de Chèque")
    date_ch = fields.Datetime(string="Date Chèque")
    num_traite = fields.Char(string="Numéro de Traite")
    date_traite = fields.Datetime(string="Date Traite")
    date_vir = fields.Datetime(string="Date Virement")

    @api.depends('notification_bill')
    def _compute_len_products(self):
        for label in self:
            summa = self.env['account.notification'].search_count([('notification', '=', self.bill.id)])
            if summa < 1:
                label.leng = False
            else:
                label.leng = True
            print(summa)

    leng = fields.Boolean(compute=_compute_len_products)

    def post(self):
        if self.notification_bill:
            paid = self.env['account.notification'].search([('id', '=', self.notification_bill.id)])
            paid.paid = True
        else:
            self.env['account.notification'].sudo().create({
                'notification': self.bill.id,
                'date': date.today(),
                'paid': True,
                'channel': None,
                'amount': self.amount,
            })
        """ Create the journal items for the payment and update the payment's state to 'posted'.
            A journal entry is created containing an item in the source liquidity account (selected journal's default_debit or default_credit)
            and another in the destination reconcilable account (see _compute_destination_account_id).
            If invoice_ids is not empty, there will be one reconcilable move line per invoice to reconcile with.
            If the payment is a transfer, a second journal entry is created in the destination journal to receive money from the transfer account.
        """
        AccountMove = self.env['account.move'].with_context(default_type='entry')
        for rec in self:

            if rec.state != 'draft':
                raise UserError(_("Only a draft payment can be posted."))

            if any(inv.state != 'posted' for inv in rec.invoice_ids):
                raise ValidationError(_("The payment cannot be processed because the invoice is not open!"))

            # keep the name in case of a payment reset to draft
            if not rec.name:
                # Use the right sequence to set the name
                if rec.payment_type == 'transfer':
                    sequence_code = 'account.payment.transfer'
                else:
                    if rec.partner_type == 'customer':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.customer.invoice'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.customer.refund'
                    if rec.partner_type == 'supplier':
                        if rec.payment_type == 'inbound':
                            sequence_code = 'account.payment.supplier.refund'
                        if rec.payment_type == 'outbound':
                            sequence_code = 'account.payment.supplier.invoice'
                rec.name = self.env['ir.sequence'].next_by_code(sequence_code, sequence_date=rec.payment_date)
                if not rec.name and rec.payment_type != 'transfer':
                    raise UserError(_("You have to define a sequence for %s in your company.") % (sequence_code,))

            moves = AccountMove.create(rec._prepare_payment_moves())
            moves.filtered(lambda move: move.journal_id.post_at != 'bank_rec').post()

            # Update the state / move before performing any reconciliation.
            move_name = self._get_move_name_transfer_separator().join(moves.mapped('name'))
            rec.write({'state': 'posted', 'move_name': move_name})

            if rec.payment_type in ('inbound', 'outbound'):
                # ==== 'inbound' / 'outbound' ====
                if rec.invoice_ids:
                    (moves[0] + rec.invoice_ids).line_ids \
                        .filtered(
                        lambda line: not line.reconciled and line.account_id == rec.destination_account_id and not (
                                line.account_id == line.payment_id.writeoff_account_id and line.name == line.payment_id.writeoff_label)) \
                        .reconcile()
            elif rec.payment_type == 'transfer':
                # ==== 'transfer' ====
                moves.mapped('line_ids') \
                    .filtered(lambda line: line.account_id == rec.company_id.transfer_account_id) \
                    .reconcile()
        return True

    @api.onchange('notification_bill')
    def _get_amount(self):
        if self.notification_bill:
            bill = self.notification_bill.id
            cash = self.env['account.notification'].search([('id', '=', bill)])
            self.amount = cash.amount

    def _create_payment_vals_from_wizard(self):
        if self.notification_bill:
            payment_vals = {
                'date': self.payment_date,
                'amount': self.amount,
                'payment_type': self.payment_type,
                'partner_type': self.partner_type,
                'ref': self.communication,
                'journal_id': self.journal_id.id,
                'currency_id': self.currency_id.id,
                'partner_id': self.partner_id.id,
                'partner_bank_id': self.partner_bank_id.id,
                'payment_method_id': self.payment_method_id.id,
                'destination_account_id': self.line_ids[0].account_id.id,
                'num_ch': self.notification_bill.number,
                'num_lc': self.notification_bill.num,
                'type_pay': self.bill.type1

            }
        else:
            payment_vals = {
                'date': self.payment_date,
                'amount': self.amount,
                'payment_type': self.payment_type,
                'partner_type': self.partner_type,
                'ref': self.communication,
                'journal_id': self.journal_id.id,
                'currency_id': self.currency_id.id,
                'partner_id': self.partner_id.id,
                'partner_bank_id': self.partner_bank_id.id,
                'payment_method_id': self.payment_method_id.id,
                'destination_account_id': self.line_ids[0].account_id.id,
                'payment_mode': self.payment_mode,
                'num_ch': self.num_ch,
                'date_ch': self.date_ch,
                'num_traite': self.num_traite,
                'date_traite': self.date_traite,
                'date_vir': self.date_vir

            }

        if not self.currency_id.is_zero(self.payment_difference) and self.payment_difference_handling == 'reconcile':
            payment_vals['write_off_line_vals'] = {
                'name': self.writeoff_label,
                'amount': self.payment_difference,
                'account_id': self.writeoff_account_id.id,
            }
        return payment_vals

    def action_create_payments(self):
        payments = self._create_payments()
        if self.notification_bill:
            paid = self.env['account.notification'].search([('id', '=', self.notification_bill.id)])
            paid.paid = True
        if self._context.get('dont_redirect_to_payments'):
            return True

        action = {
            'name': _('Payments'),
            'type': 'ir.actions.act_window',
            'res_model': 'account.payment',
            'context': {'create': False},
        }
        if len(payments) == 1:
            action.update({
                'view_mode': 'form',
                'res_id': payments.id,
            })
        else:
            action.update({
                'view_mode': 'tree,form',
                'domain': [('id', 'in', payments.ids)],
            })
        return action


class AccountInvoiceInherit(models.Model):
    _inherit = 'account.move'

    notification_bill = fields.One2many(
        'account.notification',
        'notification'

    )
    channel = fields.Many2one(
        'mail.channel',
        domain=[('channel_type', '=', 'channel')],
    )
    installments_total = fields.Float(
        compute='_compute_installments',
    )
    remaining = fields.Float(
        compute='_compute_remaining'
    )
    type1 = fields.Selection([('ch', 'Chèque'), ('lc', 'Lettre de Change')], index=True)

    def _compute_installments(self):
        for rec in self:
            total = 0
            cashes = self.env['account.notification'].search([('notification', '=', rec.id)])
            for cash in cashes:
                total = total + cash.amount
            rec.installments_total = total

    def _compute_remaining(self):
        for rec in self:
            remain = rec.amount_total - rec.installments_total
            rec.remaining = remain

    @api.onchange('channel')
    def _channels(self):
        bill = self._origin.id
        dates = self.env['account.notification'].search([('notification', '=', bill)])
        for data in dates:
            data.channel = self.channel

    @api.constrains('notification_bill')
    def _max_notification_bill(self):
        for rec in self:
            total = 0
            cashes = self.env['account.notification'].search([('notification', '=', self.id)])
            for cash in cashes:
                total = total + cash.amount
            if total > rec.amount_total:
                raise ValidationError('Installments Total is more than the invoice Total.')


class Notification(models.Model):
    _name = "account.notification"
    _description = "Paiement à terme"

    name = fields.Char(
        string='Name',
        compute='_compute_name',
    )
    notification = fields.Many2one(
        comodel_name='account.move',
        ondelete="cascade"
    )
    date = fields.Datetime(
        required=True
    )
    paid = fields.Boolean(string='Payé')
    amount = fields.Float(string='Montant')
    channel = fields.Many2one('mail.channel')
    number = fields.Char(string='Numéro de Chèque', size=7)
    num = fields.Char(string='Numéro de traite', size=12)

    _sql_constraints = [('numero_unique', 'UNIQUE(number)', "Le numéro de Chèque de change doit être unique"), ]
    _sql_constraints = [('num_unique', 'UNIQUE(num)', "Le numéro de Lettre de Change doit être unique"), ]

    @api.depends("notification.type1")
    def _compute_name(self):
        if self.notification.type1 == 'ch':
            for rec in self:
                rec.name = str(rec.number)
        else:
            for rec in self:
                rec.name = str(rec.num)
        # + "/" + str(rec.date.strftime('%d-%m-%Y'))

    def vendor_notification(self):
        dates = self.env['account.notification'].search([('date', '<=', date.today()), ('paid', '!=', True)])
        for data in dates:
            if data.channel:
                body = 'Please be informed that the (invoice/bill) ' + data.notification.name + ' has a due payment on date ' + data.date.strftime(
                    '%d-%m-%Y') + ' With the amount ' + str(data.amount)
                data.channel.message_post(body=body, subtype='mt_comment', author_id=2)


class payments(models.Model):
    _inherit = 'account.payment'

    num_ch = fields.Char(string="Numéro de Chèque")
    num_lc = fields.Char(string="Numéro de Lettre de Change")
    type_pay = fields.Selection([('esp', 'Espèce'), ('ch', 'Chèque'), ('vir', 'Virement'), ('lc', 'Lettre de change')])
    payment_mode = fields.Selection(
        selection=[('change', 'Espèce'), ('cheque', 'Chèque'), ('vir', 'Virement'), ('traite', 'Traite')])
    num = fields.Char()
    date_ch = fields.Datetime(string="Date Chèque")
    num_traite = fields.Char(string="Numéro de Traite")
    date_traite = fields.Datetime(string="Date Traite")
    date_vir = fields.Datetime(string="Date Virement")

