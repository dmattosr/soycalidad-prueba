# Prueba técnica Odoo

Odoo ver. 16

Desarrollada por Daniel Mattos
Nombre del addon `soycalidad`

# Instalación

Instalar el addon `soycalidad`


## Parte 1

Agregar al listado de clientes una columna con el campo “Idioma” de contacto (módulo
point_of_sale)

![Parte 1](/images/Parte-1.png)

## Parte 2

Agregar una validación (alerta) al POS cuando se seleccione un producto con precio S/ 0.0 
(módulo point_of_sale)

![Parte 2](/images/Parte-2.png)

## Parte 3

Crear un módulo que agregue un botón “Boleta” en el PaymentScreen (módulo
point_of_sale)

![Parte 3](/images/Parte-3.png)

## Parte 4
Agregar QR con Número factura + “|” + Nombre Cliente + “|” + Fecha Factura + “|” + [TOTAL CANTIDADES
DE LÍNEA] + “|” + Total a pagar

![Parte 4](/images/Parte-4.png)

## Parte 5

Agregar dos campos a la factura Número de serie y número correlativo.

![Parte 5](/images/Parte-5.png)

## Parte 6

Agregar un campo Canal de ventas, colocarlo debajo del campo Vendedor.

![Parte 6](/images/Parte-6.png)

## Parte 7

Ocultar el campo Fecha de la factura y reemplazarlo por Fecha de emisión, este nuevo
campo no solo debe tener la fecha sino también la hora. (módulo account)

![Parte 7](/images/Parte-7.png)

## Parte 8

Los cambios solicitados en los puntos 5, 6 y 7 deben también incluirse en el reporte impreso
de la factura

![Parte 8](/images/Parte-8.png)

## Parte 9

Agregar un campo Many2many en la factura con todos las transferencias (stock.picking)
relacionadas al pedido de venta que originó la factura.

![Parte 9](/images/Parte-9.png)

