{
    "name": "Servicing24 Reports Customization",
    "version": "1.1",
    "author": "Abrar Ahmed Tian",
    "summary": "Serviving24 Reports Customization",
    "website": "https://metamorphosis.com.bd",
    "sequence": 7,
    "license": "AGPL-3",
    "description": "Serviving24 Reports Customization",
    "depends": [ "account", "sale", "stock", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/company_delivery_slip.xml",
        "views/company_invoice_bill.xml",
        "views/employee_view.xml",
        "views/company_sale_order.xml",
        "views/res_company_qr_code.xml",
        "views/company_payment_slip.xml",
        "report/company_invoice_bill_report.xml",
        "report/company_delivery_slip_report.xml",
        "report/company_sale_order_report.xml",
        "report/Invoice_without_letterhead_report.xml",
        "report/deliveryslip_without_letterhead.xml",
        "report/sale_order_without_letterhead_report.xml",
        "report/custom_payment_receipt.xml",
    ],
    "installable": True,
    "application": True,
}