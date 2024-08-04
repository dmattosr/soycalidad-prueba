odoo.define('soycalidad.PaymentScreen', function (require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    const { Gui } = require('point_of_sale.Gui');

    const PosBoletaButtonPaymentScreen = (PaymentScreen) =>
        class extends PaymentScreen {
            async onClickBoleta() {
                const total = this.currentOrder.get_total_with_tax();
                Gui.showPopup('ConfirmPopup', {
                    title: 'Total a pagar',
                    body: `El total a pagar es "${total.toFixed(2)}" .`,
                });
            }
        };

    Registries.Component.extend(PaymentScreen, PosBoletaButtonPaymentScreen);

    return PosBoletaButtonPaymentScreen;
});
