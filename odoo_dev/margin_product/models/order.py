from odoo import api, fields, models


class MarginOrder(models.Model):
    _inherit = 'sale.report'

    # order_id = fields.Many2one('sale.order', 'Order #', readonly=True)
    # # order_line_ids = fields.One2many('sale.order.line', 'order_id' ,'Order Line', readonly=True)
    # order_line_id = fields.Many2one('sale.order.line','Order Line', readonly=True)

    # def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
    #     from_clause += ',join res_user on l.user_ids=user.id'
    #     groupby += ',l.order_id'
    #     return super(MarginOrder, self)._query(with_clause, fields, groupby, from_clause)








