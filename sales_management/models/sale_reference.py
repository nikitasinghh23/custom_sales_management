from odoo import models, fields
from odoo import exceptions


class AccountMove(models.Model):
    _inherit = 'account.move'

    reference_id = fields.Char(string="Reference ID", readonly=True)
