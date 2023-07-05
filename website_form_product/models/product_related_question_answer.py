#  Copyright 2023 GUMBYS
#  @author Gianni De Leeuw <gianni.deleeuw@gumbys.be>
#  License 'OEEL-1' or later.

from odoo import fields, models


class ProductRelatedQuestionAnswer(models.Model):
    _name = "product.related.question.answer"
    _description = "Product related answers"

    name = fields.Char()
    question_id = fields.Many2one(
        "product.related.question",
        string="Question",
        ondelete="cascade",
        required=True,
        index=True,
    )
