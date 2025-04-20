
from odoo import api, models, fields, _


class FieldWidgets(models.Model):
    """Need of this model is because we can't filter a selection field dynamically
       so when we select a field its widgets also need to change according to field
       type, we can't do it by a 'selection' field, need a 'Many2one' field."""

    _name = 'field.widgets'
    _description = 'Field Widgets'
    _rec_name = 'description'

    name = fields.Char(string="Nom")
    description = fields.Char(string="Description")



