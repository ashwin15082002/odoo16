# -*- coding: utf-8 -*-

{
    'name': "Custom Gantt View",
    'version': '16.0.1.0.0',
    'depends': ['base', 'project'],
    'author': "Ashwin",
    'category': 'category',
    'description': """  """,
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/gantt_views.xml',
        'views/gantt_view_action.xml',

    ],
}
