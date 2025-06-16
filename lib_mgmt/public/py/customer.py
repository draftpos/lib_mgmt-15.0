import frappe
from frappe import _

def get_member(doc,event):
	diff = frappe.db.get_single_value('Library Settings','default_membership_type')
	if doc.is_member == 1:
		get_member = frappe.db.get_value('Member', {'customer_name':doc.name}, ['customer_name'])
		if get_member:
			member_id = frappe.db.get_value('Member', {'customer_name':doc.name}, ['name']);
			get_doc = frappe.get_doc("Member",member_id)
			get_doc.customer = doc.customer_name
			get_doc.email_id = doc.email_id
			get_doc.save()
		else:
			new_doc = frappe.new_doc("Member")
			new_doc.member_name = doc.customer_name
			new_doc.customer = doc.customer_name
			new_doc.email_id = doc.email_id
			new_doc.membership_type = diff
			new_doc.insert()