{
    # 模块名称
    'name': 'My Minimal Demo BoluChat',
    # 模块版本
    'version': '18.0.1.0.0',
    # 简短介绍
    'summary': 'Minimal demo module for Odoo Apps Store',
    # 详细介绍
    'description': """
        Minimal test module to publish on apps.odoo.com
    """,
    # 作者
    'author': 'Sarah/Bolutech',
    # 价格配置
    'price': 9.99,
    'currency': 'EUR', # 只支持 EUR / USD，默认EUR，最低 9 EUR
    # 付费模块建议许可证改为 OPL-1
    'license': 'OPL-1',
    # 分类：模块分类，默认Uncategorized，建议使用Sales Management或Project Management
    'category': 'Sales Management',
    # 依赖：如果你的模块依赖sales模块，depends加上'sales'
    'depends': [
        'base',
        'sale'
    ],
    # 数据：如果你的模块有xml视图，放在这里
    'data': [
        # 没有xml视图就留空
    ],
    # 安装：是否可安装
    'installable': True,
    # 自动安装：是否自动安装
    'auto_install': False,
    # 应用：是否显示在应用菜单
    'application': False,
    # 图片：设置模块图片
    'images': [
        # 设置封面图片
        'images/main.jpg'
    ],
}