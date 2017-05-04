# -*- coding: utf-8 -*-
{
    'name': "sticky_table_header",

    'summary': """Sticky Table Header
        """,

    'description': """
----------------------------------------------
|              sticky_table_header           |
----------------------------------------------

Stick the list view table header on top and help to relate the table content with their header. 
Very helpful for a huge list view .

    """,

    'author': "Deepak Dixit",
    'website': "deepakdixit0001@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Widget',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
