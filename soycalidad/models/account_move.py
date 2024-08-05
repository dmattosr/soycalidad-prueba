from odoo import models, fields, api
import base64
import qrcode
import io

class AccountMove(models.Model):
    _inherit = 'account.move'

    x_qr_invoice = fields.Binary(string="QR Code", compute="_compute_qr_code")

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
