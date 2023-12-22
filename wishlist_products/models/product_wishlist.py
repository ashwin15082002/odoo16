# -*- coding: utf-8 -*-

from odoo import api, models


class WebsiteWishlist(models.Model):
    _inherit = 'product.wishlist'

    @api.model
    def _add_to_wishlist(self, pricelist_id, currency_id, website_id, price,
                         product_id, partner_id=False):
        """ This function is used to while adding products into wishlist
        also create a record in the wishlist_report model. """
        res = super()._add_to_wishlist(pricelist_id, currency_id, website_id,
                                       price, product_id, partner_id)
        self.env['wishlist.report'].create({'partner_id': res.partner_id.id,
                                            'product_id': res.product_id.id})
