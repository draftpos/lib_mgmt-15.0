import frappe
from frappe import _

def allow_books(doc,event):
	al = frappe.db.get_single_value('Library Settings', 'allow_books');
	pen = frappe.get_doc('Customer',doc.customer)
	# link = ('<a href=/app/sales-invoice/{0}>{1}</a>').format(doc.name,doc.name)
	if doc.total_qty > al:
		frappe.throw("You can not take a more than "+ str(al) +" Book")
	if pen.total_books < al:
		pen.total_books = pen.total_books + doc.total_qty
		pen.save() 
	else:
		frappe.throw("You have Reached your Limit Of Lending Book !!!! ")

def get_penalty(doc,event):
	if doc.is_return == 1:
		if doc.overdue_penalty > 0:
			query = frappe.qb.from_('Customer').select('id', 'fname', 'lname', 'phone')
			values = {'overdue_penalty': doc.overdue_penalty}
			data = frappe.db.sql("""
		    SELECT
		        pt.name
		            from `tabPenalty Template` pt
		        WHERE
		            %(overdue_penalty)s BETWEEN pt.no_of_day_penalty_from AND pt.no_of_day_penalty_to
			""",values=values,as_dict=0)
			doc.penalty_template = data
			print(":::::::::::::::::::::Penalty Amount ::::::::::::::",data)
			if data:
				doc.penalty_template = data[0][0]
				pen_amt = frappe.db.get_value('Penalty Template', {'name': doc.penalty_template}, ['penalty_amount'])
				doc.penalty_amount = pen_amt
				doc.penalty_total_amount = pen_amt * (-doc.total_qty)
				
def penalty_create(doc,event):
	if doc.penalty_amount > 0:
		pci = frappe.db.get_single_value('Library Settings','penalty_charge_item')
		staff = frappe.db.get_single_value('Library Settings','staff')
		if staff != doc.customer_group:
			if not pci:
				frappe.throw("Please set the Penalty Charge Item in Library Settings")
			else:
				new_si = frappe.new_doc("Sales Invoice")
				new_si.is_penalty = 1
				new_si.naming_series = "ACC-SINV-PEN-.YYYY.-"
				new_si.customer = doc.customer
				new_si.due_date = doc.due_date
				new_si.sales_return_id = doc.name
				main_si = ('<a onclick="window.open(this.href);return false;" href=/app/sales-invoice/{0}>{1}</a>').format(doc.return_against,doc.return_against)
				ret_si = ('<a onclick="window.open(this.href);return false;" href=/app/sales-invoice/{0}>{1}</a>').format(doc.name,doc.name)
				pen_temp = ('<a onclick="window.open(this.href);return false;" href=/app/sales-invoice/{0}>{1}</a>').format(doc.penalty_template,doc.penalty_template)
				for d in doc.get('items'):
					des = ("Sales Invoice: {0},<br>Return Invoice: {1},<br>Penalty Template: {2}, <br>Penalty Amount: {3}, <br>Total Penalty Amount: {4} \
						<br><br> <b>Items:</b><br>Item Code: {5}").format(main_si, ret_si, pen_temp, doc.penalty_amount, doc.penalty_total_amount, d.item_code)
					rows = new_si.append('items', {})
					rows.item_code = pci
					rows.qty = 1
					rows.rate = doc.penalty_amount
					rows.description = des
				new_si.insert()				
