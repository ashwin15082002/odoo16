# -*- coding: utf-8 -*-

{
    'name': "Wishlist Products",
    'version': '16.0.4.0.0',
    'depends': ['website','website_sale'],
    'author': "Ashwin",
    'category': 'website',
    'description': """ Wish list product of customers on the website. 
                        When a customer adds products to wishlist, 
                        the administrator can track them from the Reporting > Wishlist product.""",

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/wishlist_products_views.xml',
        'views/action_wishlist_reporting.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',

}
