from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    # override
    sequence_id = fields.Many2one(help="This sequence is automatically created by Viindoo but you can change it "
        "to customize the reference numbers of your orders.")
    sequence_line_id = fields.Many2one(help="This sequence is automatically created by Viindoo but you can change it "
        "to customize the reference numbers of your orders lines.")
