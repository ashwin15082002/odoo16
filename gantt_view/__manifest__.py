# -*- coding: utf-8 -*-

{
    'name': "Custom Gantt View",
    'version': '16.0.1.0.0',
    'depends': ['base', 'project', 'web'],
    'author': "Ashwin",
    'category': 'category',
    'description': """ Custom gantt view for project module. """,
    'installable': True,
    'application': False,
    'license': 'LGPL-3',

    'data': ['views/project_gantt_view.xml',],
    'assets': {
        'web.assets_backend': [
            'gantt_view/static/src/xml/gantt_view.xml',
            'gantt_view/static/src/js/gantt_view.js',
        ],
    }
}
