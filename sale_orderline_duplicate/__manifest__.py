{
    'name': "Sale Orderline Duplicate",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Amzsys",
    'website': "https://www.amzsys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.10',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'views/orderline_duplicate.xml'
    ],
    'images':[
        'images/cover-salelinedup.png',
        ],
    # only loaded in demonstration mode

    'demo': [
        'demo/demo.xml',
    ],
    "license": "OPL-1",
}
