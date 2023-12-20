# -*- coding: utf-8 -*-

{
    'name': "Average Landed Cost",
    'version': '16.0.1.0.0',
    'depends': ['base', 'stock', 'sale_management', 'purchase'],
    'author': "Ashwin",
    'category': 'inventory',
    'description': """ Calculate average landed cost """,
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/landed_cost_views.xml',
    ],
}
