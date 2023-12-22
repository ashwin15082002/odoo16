# -*- coding: utf-8 -*-

from odoo.http import request

from odoo.addons.website_sale_wishlist.controllers.main import \
    WebsiteSaleWishlist


class WishlistProducts(WebsiteSaleWishlist):
    def rm_from_wishlist(self, wish, **kw):
        """ While removing the products from wishlist also removes record from
            the wishlist_report model """
        request.env['wishlist.report'].search([
            ('partner_id', '=', wish.partner_id.id), ('product_id', '=',
                                                      wish.product_id.id)]).unlink()
        super(WishlistProducts, self).rm_from_wishlist(wish, **kw)
