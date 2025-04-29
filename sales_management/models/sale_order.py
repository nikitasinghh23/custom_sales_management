from odoo import fields, models, api
from odoo import exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    reference_id = fields.Char(string="Reference ID", size=10)

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'sale':
            self.reference_id = False

    def _prepare_invoice(self):
        invoice_vals = super()._prepare_invoice()
        print("----invoice_vals---",invoice_vals)
        invoice_vals.update({
            'reference_id': self.reference_id,
        })
        print("----invoice_vals--invoice_vals--",invoice_vals)
        return invoice_vals

    def write(self, vals):
        result = super().write(vals)
        print("---result",result)
        if 'reference_id' in vals:
            print("vals",vals)
            for order in self:
                print("----self--",self)
                print("----order--", order)
                for invoice in order.invoice_ids:
                    print("----invoice---",invoice)
                    invoice.reference_id = vals['reference_id']
        return result