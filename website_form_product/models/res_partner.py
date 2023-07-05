#  Copyright 2023 GUMBYS
#  @author Gianni De Leeuw <gianni.deleeuw@gumbys.be>
#  License 'OEEL-1' or later.

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_b2b_partner = fields.Boolean()
