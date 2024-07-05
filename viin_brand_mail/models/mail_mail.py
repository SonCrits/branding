from odoo import fields, models


class MailMail(models.Model):
    _inherit = 'mail.mail'

    auto_delete = fields.Boolean(help="This option permanently removes any track of email after it's been sent, "
        "including from the Technical menu in the Settings, in order to preserve storage space of your Viindoo database.")
