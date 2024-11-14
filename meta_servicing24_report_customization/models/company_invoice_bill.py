from odoo import fields, models, api



class EmployeeBill(models.Model):
   _inherit = "account.move"

   billed_by_em = fields.Many2one('hr.employee', string="Billed by")
   contact_person_id = fields.Many2one('res.partner', string="Contact Person",  domain="[('parent_id', '=', partner_id)]")
   contact_person_name = fields.Char(related="contact_person_id.name", string="Contact Person Name")
   contact_person_email = fields.Char(related="contact_person_id.email", string="Contact Person Email")
   contact_person_phone = fields.Char(related="contact_person_id.mobile", string="Contact Person Phone")  
   authorized_sign = fields.Binary(related="billed_by_em.sale_signature")

   image_qr_code = fields.Binary(related="company_id.qr_code_image", string = "Image", store=True)

#    seq Test
#    prefix = fields.Char(string="Invoice Prefix", default="#SCL/24/INV-")

#    custom_invoice_number = fields.Char(string='Custom Invoice Number', compute='_compute_custom_invoice_number')
#    @api.depends('name','prefix')
#    def _compute_custom_invoice_number(self):
#     for record in self:
#             parts = record.name.split('/')
#             invoice_number_only = parts[-1]
#             record.custom_invoice_number = f"{record.prefix}{invoice_number_only}"
      
        




 
   contact_person_address = fields.Char(
        string="Contact Address",
        compute="_compute_contact_person_address",
        store=True
    )
   
  
  
   def print_invoice(self):
        return self.env.ref('account.account_invoices').report_action(self)

   @api.depends('contact_person_id')
   def _compute_contact_person_address(self):
        for record in self:
            if record.contact_person_id:
                partner = record.contact_person_id
                address = [
                    partner.street,
                    partner.street2,
                    partner.city,
                    partner.state_id.name,
                    partner.zip,
                    partner.country_id.name,
                ]
                address = [part for part in address if part]
                record.contact_person_address = ", ".join(address)
            else:
                record.contact_person_address = ""


    

class BillWarrenty(models.Model):
   _inherit = "account.move.line"
   lot_serial_number_id = fields.Many2one('stock.lot', domain="[('product_id', '=', product_id)]")
   warrenty = fields.Char(string="Warrenty")

