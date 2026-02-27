from odoo import models, fields

class EstateProperty(models.Model):
    _inherit = 'estate.property'

    def action_sold(self):
        partner = self.buyer_id

        self.env['account.move'].create(
            {
                'partner_id': partner.id,
                'move_type': 'out_invoice',
                'invoice_date': fields.Date.today(),
                "invoice_line_ids":[
                    (0, 0, {
                        'name': "6% of selling price",
                        'quantity': 1,
                        'price_unit': self.selling_price * 0.06,}),
                    (0, 0, {
                        'name': 'administrative fees',
                        'quantity': 1,
                        'price_unit': 100.00,})
                ]
            }
        )
        

        return super().action_sold()