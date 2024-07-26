from typing import Optional

from odoo import models
from odoo.addons.base.models.ir_qweb_fields import Markup



class PosSession(models.Model):
    _inherit = 'pos.session'

    def _get_unprocessed_pos_order_scheduled_activity(self, order_ref: str, pos_order_data_hash: int, assigned_user_id: Optional[int] = None, create: bool = True):
        res = super(PosSession, self)._get_unprocessed_pos_order_scheduled_activity(order_ref, pos_order_data_hash, assigned_user_id, create)
        if res:
            if 'Odoo' in res.note:
                res.note = Markup(res.note).striptags().replace('Odoo', 'Viindoo')
        return res
