{
    'name' : 'Puerto PME',
    'version' : '1.0.0',
    'category' : 'Puerto',
    'description' : """ Test Module to understand odoo stracture more """,
    'depends' : [], 
    'data'    : ['views/menu.xml',
                 'security/ir.model.access.csv',

],
 'web.assets_backend': [
    '/opt/odoo15/odoo/customs/puertopme/static/src/css/style.css',
],

    
    'installable' : True,
    'auto_install' : False,
    'license' : 'AGPL-3',
}
