import frappe
from frappe import _

def get_membership(doc, event):
	pr = frappe.new_doc('Pricing Rule')
	pr.title = doc.member_name 
	pr.valid_from = doc.from_date
	pr.valid_upto = doc.to_date
	pr.selling = 1
	pr.applicable_for = "Customer"
	pr.customer = doc.member_name
	pr.for_price_list = doc.membership_type
	ig = frappe.db.get_list('Item Group')
	# for d in ig:
		# ir = frappe.get_doc('Item Group',d)
	pr.append('item_groups',{
		'item_group': 'All Item Groups'
	})
	pr.insert()