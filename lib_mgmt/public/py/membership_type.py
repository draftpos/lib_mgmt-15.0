import frappe
from frappe import _

def pricing_list(doc,event):
	pr_ls = frappe.new_doc("Price List")
	pr_ls.price_list_name = doc.membership_type
	pr_ls.selling = 1
	pr_ls.rate_or_discount = "Discount Percentage"
	pr_ls.discount_amount = doc.amount
	pr_ls.insert()