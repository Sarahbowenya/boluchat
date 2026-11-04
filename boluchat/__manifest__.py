{
    'name': 'My Minimal Demo BoluChat',
    'version': '18.0.1.0.0',
    'summary': 'Minimal demo module for Odoo Apps Store',
    'description': """
        Minimal test module to publish on apps.odoo.com
    """,
    'author': 'Sarah/Bolutech',
    'license': 'LGPL-3',
    'category': 'Uncategorized',
    'depends': [
        'base',
        'sale'
    ],
    'data': [
        # 没有xml视图就留空
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'images': [
        'images/main.jpg'
    ],
}