# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    duplicate_check = fields.Boolean(
        "Enable duplicate check", default=True)
    duplicate_check_fields = fields.Many2many('res.partner.fields', string="Champs à vérifier")
    user_whitelist = fields.Many2many('res.users', string="Utilisateurs avec vérification des doublons désactivée")

    def set_values(self):
        self.ensure_one()
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('contact_deduplicate.duplicate_check', self.duplicate_check)
        self.env['ir.config_parameter'].sudo().set_param('contact_deduplicate.duplicate_check_fields', self.duplicate_check_fields.ids)
        self.env['ir.config_parameter'].sudo().set_param('contact_deduplicate.user_whitelist', self.user_whitelist.ids)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        get_param = self.env['ir.config_parameter'].sudo().get_param
        res['duplicate_check'] = get_param('contact_deduplicate.duplicate_check')
        f_ids = get_param('contact_deduplicate.duplicate_check_fields')
        if f_ids:
            res['duplicate_check_fields'] = eval(f_ids)
        u_ids = get_param('contact_deduplicate.user_whitelist')
        if u_ids:
            res['user_whitelist'] = eval(u_ids)
        return res