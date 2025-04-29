{
    'name': 'sales_management',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Custom Sales Module for Odoo 18',
    'description': """
    This is a custom sales module for Odoo 18.
    """,
    'author': 'odoo ',
    'website': 'https://www.example.com',
    'depends': ['sale','base'],
    'data': [
        'security/ir.model.access.csv',
        # 'security/record_rule.xml',
        'views/sale_order_view.xml',
        'views/sale_invoice_view.xml',
        # 'views/menu_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
