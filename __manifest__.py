# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Odoo app to manage an academy.""",

    'description': """
        The citadel of the seven kingdoms, located in Oldtown would like to use Odoo to manage the training of its future maesters. In this system, the citadel wants to create and edit classes, with different levels. They would like to handle different sessions given by different maesters at different moments. It would be nice to register the attendees of those sessions.
    """,

    'author': "Gautham.Y",
    'website': "http://www.google.com/odoo",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/menu_views.xml',
        'data/courses.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}