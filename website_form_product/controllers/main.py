#  Copyright 2023 GUMBYS
#  @author Gianni De Leeuw <gianni.deleeuw@gumbys.be>
#  License 'OEEL-1' or later.
import json

from odoo import SUPERUSER_ID
from odoo.http import request

from odoo.addons.website_crm.controllers import website_form


class WebsiteForm(website_form.WebsiteForm):
    def extract_data(self, model, values):
        """
        Add the custom fields to the custom answers field in the crm app
        """
        data = super().extract_data(model, values)

        authorized_fields = model.with_user(SUPERUSER_ID)._get_form_writable_fields()
        model_field = model.field_id.filtered(lambda f: f.name == "custom_answers")
        # DUmmy commit
        if model_field:
            custom_fields = {}

            for field_name, field_value in values.items():
                if (
                    field_name != "context"
                    and field_name not in authorized_fields
                    and not hasattr(field_value, "filename")
                ):
                    question_name = (
                        request.env["product.related.question"]
                        .sudo()
                        .search([("name", "=", field_name)])
                    )

                    if question_name:
                        custom_fields[field_name] = field_value

            data["record"]["custom_answers"] = json.dumps(custom_fields)

        return data
