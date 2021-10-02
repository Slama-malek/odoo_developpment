from odoo import api, fields, models


class MarginSaleOrder(models.Model):
    _inherit = 'sale.order.line'

    product_template_id = fields.Many2one(
        'product.template', string='Product Template',
        related="product_id.product_tmpl_id", domain=[('sale_ok', '=', True)])
    sales_margin = fields.Float(String='Sales Margin', readonly=False)
    price_unit = fields.Float('Unit Price')
    user_ids = fields.Many2many('res.users', string='Salesperson', index=True, tracking=2,
                                default=lambda self: self.env.user)

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(MarginSaleOrder, self).product_id_change()
        vals = {}
        for line in self:
            vals['sales_margin'] = self.product_template_id.sales_margin
            if self.product_template_id.sales_margin != 0:
                vals['price_unit'] = self.product_template_id.standard_price / self.product_template_id.sales_margin
        self.update(vals)

        return res

    @api.onchange('sales_margin')
    def sales_margin_change(self):
        if self.sales_margin != 0:
            self.price_unit = self.product_template_id.standard_price / self.sales_margin

    @api.onchange('price_unit')
    def price_unit_change(self):
        if self.price_unit != 0:
            self.sales_margin = self.product_template_id.standard_price / self.price_unit

    def _prepare_invoice_line(self, **optional_values):
        res = super(MarginSaleOrder, self)._prepare_invoice_line(**optional_values)
        vals = {'price_unit': self.price_unit,
               'sales_margin': self.sales_margin,

               }
        self.update(vals)
        return res



