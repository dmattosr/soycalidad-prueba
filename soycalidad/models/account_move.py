from odoo import models, fields, api
import base64
import qrcode
import io

separators = ['/', '-']


class SaleChannel(models.Model):
    _name = 'sale.channel'
    _description = 'Canal de ventas'

    name = fields.Char(string='Nombre del canal', required=True)


class AccountMove(models.Model):
    _inherit = 'account.move'

    x_series_number = fields.Char(string="Número de serie", compute="_compute_series_number")
    x_correlative_number = fields.Char(string="Número correlativo", compute="_compute_correlative_number")

    x_qr_invoice = fields.Binary(string="QR Code", compute="_compute_qr_code")
    sale_channel_id = fields.Many2one('sale.channel', string='Canal de ventas')
    invoice_date_issue = fields.Datetime(string='Fecha de emisión')

    @api.depends('name')
    def _compute_series_number(self):
        for record in self:
            if record.name:
                for key in separators:
                    if key in record.name:
                        parts = record.name.split(key)
                        if len(parts) > 2:
                            record.x_series_number = ''.join(parts[:-2])
                        else:
                            record.x_series_number = parts[0]
                        break

    @api.depends('name')
    def _compute_correlative_number(self):
        for record in self:
            if record.name:
                for key in separators:
                    if key in record.name:
                        record.x_correlative_number = record.name.split(key)[-1].zfill(8)
                        break

    def generate_qr_code(self, qr_string):
        qr = qrcode.QRCode(version=4, box_size=4, border=1)
        qr.add_data(qr_string)
        qr.make(fit=True)
        img = qr.make_image()
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue())
        return {'x_qr_invoice': img_str}

    @api.depends('name', 'invoice_date', 'partner_id', 'amount_total', 'invoice_line_ids')
    def _compute_qr_code(self):
        for record in self:
            x_qr_invoice = "{}|{}|{}|{}|{}".format(
                record.name,
                record.partner_id.name,
                record.invoice_date,
                sum(record.invoice_line_ids.mapped('quantity')),
                record.amount_total
            )
            record.update(self.generate_qr_code(x_qr_invoice))
