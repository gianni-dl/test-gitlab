#  Copyright 2023 GUMBYS
#  @author Gianni De Leeuw <gianni.deleeuw@gumbys.be>
#  License 'OEEL-1' or later.

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    related_question_line_ids = fields.One2many(
        "product.product.related.question.line",
        "product_id",
        "Product Related Questions",
    )
