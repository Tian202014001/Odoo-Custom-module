from odoo import api, fields, models, _

class EmployeeInherits(models.Model):
    _inherit = "hr.employee"

    sale_signature = fields.Binary("Official Signature")