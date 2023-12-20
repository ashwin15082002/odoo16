# -*- coding: utf-8 -*-

{
    'name': "Work Report Tracker",
    'version': '16.0.4.0.0',
    'depends': ['base'],
    'author': "Ashwin",
    'category': '',
    'description': """ This module is used to record the daily work reports of 
                        the employees. """,
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/work_report_views.xml',
        'views/work_report _action.xml',
    ],
}
