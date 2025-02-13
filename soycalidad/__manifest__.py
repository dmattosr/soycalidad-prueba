{
    'name': "Prueba Técnica - SoyCalidad",

    'summary': """
        Prueba Técnica
    """,
    'author': "Daniel Mattos R.",
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'sale_management',
        'point_of_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sale_channel.xml',
        'reports/report_invoice.xml',
        'views/account_move_view.xml',
    ],
    'qweb': [
        'static/src/xml/pos_boleta_button.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'soycalidad/static/src/js/models.js',
            'soycalidad/static/src/js/pos_boleta_button.js',
            'soycalidad/static/src/xml/**/*',
        ],
    },
    'application': True,
}
