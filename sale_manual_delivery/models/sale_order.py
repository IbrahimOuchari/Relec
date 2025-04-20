
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    manual_delivery = fields.Boolean(
        string="Livraison Manuelle",
        default=True,
        help="Si activé, les livraisons ne sont pas créées lors de la confirmation du SO. "
         "Vous devez utiliser le bouton Créer une livraison pour réserver et "
         "expédier la marchandise",
    )

    @api.onchange("team_id")
    def _onchange_team_id(self):
        self.manual_delivery = self.team_id.manual_delivery

    def action_manual_delivery_wizard(self):
        self.ensure_one()
        action = self.env.ref("sale_manual_delivery.action_wizard_manual_delivery")
        [action] = action.read()
        action["context"] = {"default_carrier_id": self.carrier_id.id}
        return action

    @api.constrains("manual_delivery")
    def _check_manual_delivery(self):
        if any(rec.state not in ["draft", "sent"] for rec in self):
            raise UserError(
                _(
                    "Vous ne pouvez passer que par la livraison manuelle"
                    " dans un devis, pas une commande confirmée"
                )
            )
