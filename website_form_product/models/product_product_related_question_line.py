#  Copyright 2023 GUMBYS
#  @author Gianni De Leeuw <gianni.deleeuw@gumbys.be>
#  License 'OEEL-1' or later.

from odoo import fields, models


class ProductProductRelatedQuestionLine(models.Model):
    _name = "product.product.related.question.line"
    _description = "Product Product Related Question Line"

    product_id = fields.Many2one(
        "product.product",
        string="Product Product",
        ondelete="cascade",
        required=True,
        index=True,
    )
    question_id = fields.Many2one(
        "product.related.question",
        string="Question",
        ondelete="restrict",
        required=True,
        index=True,
    )
    answer_id = fields.Many2one(
        "product.related.question.answer",
        string="Answer",
        domain="[('question_id', '=', question_id)]",
        ondelete="restrict",
    )
