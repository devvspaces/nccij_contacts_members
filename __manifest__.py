# -*- encoding: utf-8 -*-
{
    'name': 'NCCIJ Member Contacts',
    'version': '16.0',
    'category': 'Generic Modules/Others',
    'author': 'Afriquecomm',
    'depends': ['base'],
    'summary': 'NCCIJ Member Contacts',
    'description': "This module allows you to manage contacts of NCCIJ members",
    'license': 'OPL-1',
    'data': [
        'security/ir.model.access.csv',

        'views/contact_member_views.xml',
        'views/contact_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
