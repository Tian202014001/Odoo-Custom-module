from odoo import fields, models, api

class CompanyQRcode(models.Model):
   _inherit = "res.company"
   qr_code_image=fields.Binary(string="Qr Code", store=True)
   