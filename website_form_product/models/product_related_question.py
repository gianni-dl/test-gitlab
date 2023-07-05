#  Copyright 2023 GUMBYS
#  @author Gianni De Leeuw <gianni.deleeuw@gumbys.be>
#  License 'OEEL-1' or later.

from odoo import fields, models


class ProductRelatedQuestion(models.Model):
    _name = "product.related.question"
    _description = "Product related questions on a form on the website"

    name = fields.Char()
    answer_ids = fields.One2many(
        "product.related.question.answer", "question_id", "Answers", copy=True
    )
    input_select_type = fields.Selection(
        [("single", "Single Select"), ("multi", "Multi Select")],
        default="single",
    )
