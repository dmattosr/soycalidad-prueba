{
    'name': "Prueba Tecnica-SOyCalidad",

    'summary': """
        Prueba Técnica
    """,
    'author': "Daniel Mattos R.",
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',
    'depends': [
        'point_of_sale',
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
}
