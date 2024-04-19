# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Player Management',
    'version' : '1.0',
    'summary': 'player management',
    'sequence': 10,
    'description': """Manage basketball players""",
    'category': '',
    'website': '',
    'depends': ['base'],
    'data': [
        'views/player_view.xml',
        'actions/player_action.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
}
