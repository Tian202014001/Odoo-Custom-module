from odoo import fields, models, api



class StockDeliverySlip(models.Model):
   _inherit = "stock.picking"

   billed_by_em = fields.Many2one('hr.employee', string="Billed by")
   contact_person_id = fields.Many2one('res.partner', string="Contact Person",  domain="[('parent_id', '=', partner_id)]")
   contact_person_name = fields.Char(related="contact_person_id.name", string="Contact Person Name")
   contact_person_email = fields.Char(related="contact_person_id.email", string="Contact Person Email")
   contact_person_phone = fields.Char(related="contact_person_id.mobile", string="Contact Person Phone")
   authorized_sign = fields.Binary(related="billed_by_em.sale_signature")
   contact_person_address = fields.Char(
        string="Contact Address",
        compute="_compute_contact_person_address",
        store=True
    )
   image = fields.Binary(string = "Image")

   package_no = fields.Char(string="Package No:")
   package_date = fields.Date(string="Package Date:")

   total_qty = fields.Float(string="Total Qty", compute="_total_qty_sum")

   @api.depends("move_ids_without_package.quantity")
   def _total_qty_sum(self):
        for rec in self:
            if rec.move_ids_without_package:
                sum = 0
                for item in rec.move_ids_without_package:
                   
                    sum += item.quantity
                rec.total_qty = sum
  
    

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


   def print_delivery_slip(self):
        return self.env.ref('stock.action_report_delivery').report_action(self)



class BillWarrenty(models.Model):
   _inherit = "stock.move"
   warrenty = fields.Char(string="Warrenty")
#    sale_des_id = fields.Many2one('sale.order.line')
#    s_desc = fields.Text(related="sale_des_id.name")
   
