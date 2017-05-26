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

    'category': 'Widget',
    'version': '0.1',

    # Dependencies 
    'depends': ['base','web'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    
    'application': False,    
    'installable': True
}
