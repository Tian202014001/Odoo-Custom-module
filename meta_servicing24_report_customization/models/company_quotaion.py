from odoo import fields, models, api



class SaleOrderLine(models.Model):
   _inherit = "sale.order.line"

   warrenty = fields.Char(string= "Warrenty")
   lot_serial_number_id = fields.Many2one('stock.lot', domain="[('product_id', '=', product_id)]")

class SaleOrder(models.Model):
   _inherit = "sale.order"

   employee1 = fields.Many2one('hr.employee', string="Employee 1")
   employee2 = fields.Many2one('hr.employee', string="Employee 2")

   quotation_subject = fields.Text(string="Quotation Subject")
   quotation_body = fields.Html(string="Quotation Body")
   
   attn = fields.Char(stirng="Attn")

   def print_quotation(self):
        return self.env.ref('sale.action_report_pro_forma_invoice').report_action(self)

