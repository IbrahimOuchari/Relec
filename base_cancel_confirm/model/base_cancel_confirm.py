
import inspect

from lxml import etree

from odoo import fields, models


class BaseCancelConfirm(models.AbstractModel):
    _name = "base.cancel.confirm"
    _description = "Cancel Confirmation"

    _has_cancel_reason = "no"  # ["no", "optional", "required"]
    _cancel_reason_xpath = "/form/sheet/group[last()]"

    cancel_confirm = fields.Boolean(
        string="Confirmer l'Annulation",
        copy=False,
        help="Un indicateur signifie que ce document est confirmé pour l'annulation",
    )
    cancel_reason = fields.Text(
        string="Raison d'Annulation",
        copy=False,
        help="Un motif d'annulation facultatif",
    )

    def open_cancel_confirm_wizard(self):
        xmlid = "base_cancel_confirm.action_cancel_confirm_wizard"
        action = self.env["ir.actions.act_window"]._for_xml_id(xmlid)
        action["context"] = {
            "cancel_res_model": self._name,
            "cancel_res_ids": self.ids,
            "cancel_method": inspect.stack()[1][3],
            "default_has_cancel_reason": self._has_cancel_reason,
        }
        return action

    def clear_cancel_confirm_data(self):
        self.write({"cancel_confirm": False, "cancel_reason": False})

    def fields_view_get(
        self, view_id=None, view_type="form", toolbar=False, submenu=False
    ):
        res = super().fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )
        if view_type == "form":
            doc = etree.XML(res["arch"])
            for node in doc.xpath(self._cancel_reason_xpath):
                str_element = self.env["ir.qweb"]._render(
                    "base_cancel_confirm.cancel_reason_template"
                )
                new_node = etree.fromstring(str_element)
                for new_element in new_node:
                    node.addnext(new_element)
            # Override context for postprocessing
            View = self.env["ir.ui.view"]
            if view_id and res.get("base_model", self._name) != self._name:
                View = View.with_context(base_model_name=res["base_model"])
            new_arch, new_fields = View.postprocess_and_fields(doc, self._name)
            res["arch"] = new_arch
            # We don't want to loose previous configuration, so, we only want to add
            # the new fields
            new_fields.update(res["fields"])
            res["fields"] = new_fields
        return res
