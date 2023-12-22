# -*- coding: utf-8 -*-

from odoo import fields, models


class WishlistReport(models.Model):
    """ This models shows the report of products in the wishlist """

    _name = 'wishlist.report'
    _description = 'Wishlist Report'

    partner_id = fields.Many2one('res.partner', string='Owner', help='Customer')
    product_id = fields.Many2one('product.product', string='Product',
                                 help='Product')
