from odoo import api, fields, models


class MarginInvoice(models.Model):
    _inherit = 'account.move.line'

    product_id = fields.Many2one('product.product', string='Product')
    sales_margin = fields.Float('Sales Margin')
    price_unit = fields.Float(string='Unit Price')


    @api.onchange('product_id')
    def onchange_product_id(self):
        for line in self:
            line.sales_margin = self.product_id.sales_margin


    @api.onchange('sales_margin')
    def sales_margin_change(self):
        if self.sales_margin:
            self.price_unit = self.product_id.standard_price / self.sales_margin

    @api.onchange('price_unit')
    def price_unit_change(self):
        if self.price_unit :
            self.sales_margin = self.product_id.standard_price / self.price_unit



    def write(self,vals):

        res = super(MarginInvoice, self).write(vals)
        if vals.get('sales_margin'):
            self.sales_margin =vals.get('sales_margin')
        return res


