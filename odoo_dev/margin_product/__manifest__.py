# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Margin sale',
    'version' : '1.1',
    'summary': 'Margin sale',
    'description': "Margin sale",
    'category': 'Sales/Sales',
    'images' : [],
    'depends' : ['product', 'sale'],
    'data': [
        'views/product_view.xml',
        'views/sale_order_view.xml',
        'views/invoice_view.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
