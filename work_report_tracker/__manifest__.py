# -*- coding: utf-8 -*-

{
    'name': "Work Report Tracker",
    'version': '16.0.4.0.0',
    'depends': ['base','mail','web'],
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
        'data/employee_work_report.xml',
        'views/work_report_views.xml',
        'views/work_report _action.xml',
    ],
    'assets':{
        'web.assets_backend':[
            'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js',
            'work_report_tracker/static/src/xml/work_report.xml',
            'work_report_tracker/static/src/js/work_report.js',

        ]
    }
}
