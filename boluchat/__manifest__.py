{
    'name': 'My Minimal Demo BoluChat',
    'version': '18.0.1.0.0',
    'summary': 'Minimal demo module for Odoo Apps Store',
    'description': """
        Minimal test module to publish on apps.odoo.com
    """,
    'author': 'Sarah/Bolutech',
    # 价格配置 新增下面两行
    'price': 9.99,
    'currency': 'EUR', # 只支持 EUR / USD，默认EUR，最低 9 EUR
    # 付费模块建议许可证改为 OPL-1
    'license': 'OPL-1',
    'category': 'Sales Management',
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