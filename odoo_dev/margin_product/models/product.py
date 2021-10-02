from odoo import api, fields, models


class MarginProduct(models.Model):
    _inherit = 'product.template'

    sales_margin = fields.Float('Sales Margin')
    list_price = fields.Float('Sales Price',compute='_list_price')
    standard_price = fields.Float('Cost')

    @api.depends('sales_margin', 'standard_price')
    def _list_price(self):
        for record in self:
            record.list_price = 0.0
            if record.sales_margin :
                record.list_price = record.standard_price / record.sales_margin



