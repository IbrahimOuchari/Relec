from odoo import api, fields, models
class ProductSupplier(models.Model):
    _name='product.supplier'

    product=fields.Many2one('product.template',string='Produit')
    qte_stock=fields.Float(string='Quantité en Stock')
    fournisseur=fields.Many2one('res.partner',string='Fournisseur')
    qte_achete=fields.Float(string='Quantité Achetée')
    date=fields.Date(string='Date Facturation')
    price_unit=fields.Float(string='Prix Unitaire')

class MoveInheritReport(models.Model):
	_inherit='account.move'
	@api.model
	def _get_invoice_in_payment_state(self):
		res=super(MoveInheritReport,self)._get_invoice_in_payment_state()
		for rec in self:
			if rec.move_type == 'in_invoice':
				for line in rec.invoice_line_ids:
					produit = self.env['product.template'].search([('id', '=', line.product_id.id)])
					product_supplier_exist = self.env['product.supplier'].search([('product', '=', line.product_id.id),('fournisseur','=',rec.partner_id.id),('date','=',rec.invoice_date),('price_unit','=',line.price_unit)])
					if not product_supplier_exist:
						product_supplier=self.env['product.supplier'].create({'product':line.product_id.id,'qte_stock':produit.qty_available,'qte_achete':line.quantity,'fournisseur':rec.partner_id.id,'date':rec.invoice_date,'price_unit':line.price_unit})
						action={'type':'ir.actions.act_window','res_model':'product.supplier','views':[(self.env.ref('product.product_supplierinfo_form_view').id,'form')]}
					else:
						product_supplier_exist[0].qte_achete+=line.quantity
						product_supplier_exist[0].qte_stock=produit.qty_available
		return res