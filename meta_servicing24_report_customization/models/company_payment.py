from odoo import fields, models, api



class CustomerRef(models.Model):
   _inherit = "account.payment"

   customer_ref = fields.Char("For the Purpose of")