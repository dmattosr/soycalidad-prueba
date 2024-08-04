odoo.define('soycalidad.ProductScreen', function (require) {
    'use strict';

    const ProductScreen = require('point_of_sale.ProductScreen');
    const { Gui } = require('point_of_sale.Gui');
    const Registries = require('point_of_sale.Registries');

    const CustomProductScreen = (ProductScreen) =>
        class extends ProductScreen {
            async _clickProduct(event) {
                await super._clickProduct(event);

                const product = event.detail;
                if (product.lst_price <= 0) {
                    Gui.showPopup('ErrorPopup', {
                        title: 'Producto sin precio',
                        body: `El producto "${product.display_name}" no tiene precio.`,
                    });
                }
            }
        };

    Registries.Component.extend(ProductScreen, CustomProductScreen);

    return CustomProductScreen;
});
