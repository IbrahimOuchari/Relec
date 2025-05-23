from odoo import api, fields, models, _
from odoo.exceptions import UserError
import base64

class DocumentType(models.Model):
    _name = 'document.type'
    _description = 'Type Documents'

    name = fields.Char(string='Nom', required=1)
    exp_bool=fields.Boolean(string='Date Expiration ?')

class DocumentStorageLocation(models.Model):
    _name = 'document.storage.location'
    _description = 'Document Location'
    _rec_name = 'dir_location'

    name = fields.Char(string='Nom')
    document_type_id = fields.Many2one('document.type', string='Type Documents', required=1)
    dir_location = fields.Char(string='Chemin du Dossier', required=1)


class DocumentStorage(models.Model):
    _name = 'document.storage'
    _description = 'Stockage Documents'

    document_type_id = fields.Many2one('document.type', string='Type Documents',required=1)
    document_location_id = fields.Many2one('document.storage.location', string='Emplacement de Stockage',required=1)
    partner_id = fields.Many2one('res.partner', string='Partenaire')
    document_file = fields.Binary(string='Télécharger Document')
    expiry_date = fields.Date(string='Date Expiration')
    expiration_bool = fields.Boolean(string='Expiration ?', related='document_type_id.exp_bool')
    employee_id = fields.Many2one('hr.employee', string='Employée')
    name = fields.Char('Nom Document')

    @api.model
    def create(self, values):
        result = super(DocumentStorage, self).create(values)
        result._action_store_document_dir()
        return result

    def write(self, vals):
        result = super().write(vals)
        self._action_store_document_dir()
        return result

    # store document on local dir
    def _action_store_document_dir(self):
        for record in self:
            if record.document_file:
                document_file = record.document_file
                if not record.document_location_id:
                    raise UserError('Location not defined..!!')
                file_location = record.document_location_id.dir_location
                if record.partner_id:
                    name = record.partner_id.name
                elif record.employee_id:
                    name = record.employee_id.name
                file_with_location = str(file_location) + '/' + str(name)+' Document: '+str(record.name)
                try:
                    with open(file_with_location, 'wb') as f:
                        f.write(base64.b64decode(document_file))
                        f.close()
                except:
                    raise UserError('Directory does not have Permissions! Please give Permissions to store file!!')
            else:
                raise UserError('Document not found.')
                