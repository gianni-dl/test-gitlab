#  Copyright 2023 GUMBYS
#  @author Gianni De Leeuw <gianni.deleeuw@gumbys.be>
#  License 'OEEL-1' or later.
import json

from odoo import _, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    custom_answers = fields.Char()

    def action_new_quotation(self):
        """
        Search the corresponding product related to the answers from the form.
        If a product was found, add this to the new quotation.
        """
        action = super().action_new_quotation()

        if not self.custom_answers:
            return action

        question_params = json.loads(self.custom_answers)
        domain = self._prepare_product_domain(question_params)

        if not domain:
            return action

        products = self.env["product.product"].search(domain)

        if not products:
            return action

        order_id = self.env["sale.order"].with_context(action["context"]).create({})

        for product in products:
            self.env["sale.order.line"].create(
                {
                    "product_id": product.id,
                    "order_id": order_id.id,
                }
            )

        if order_id.partner_id.is_b2b_partner:
            order_id.action_confirm()

        return {
            "type": "ir.actions.act_window",
            "name": _("Sale Order"),
            "res_model": "sale.order",
            "views": [[False, "form"]],
            "res_id": order_id.id,
        }

    def _prepare_product_domain(self, question_params):
        """
        Build the product domain based on the answers. Check if the answer is
        single or multi select. When multiselect change the operator to 'in'.
        """
        domain = []
        for k, v in question_params.items():
            domain.append(("related_question_line_ids.question_id", "=", k))
            question = self.env["product.related.question"].search(
                [("name", "=", k)], limit=1
            )
            if question.input_select_type == "multi":
                domain.append(
                    ("related_question_line_ids.answer_id", "in", v.split(","))
                )
            else:
                domain.append(("related_question_line_ids.answer_id", "=", v))

        return domain
