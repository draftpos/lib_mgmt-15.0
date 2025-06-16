# import frappe
# from frappe import _

# def get_employee(doc, event):
# 	def_ter = frappe.db.get_single_value('Library Settings','default_territory')
# 	def_pr = frappe.db.get_single_value('Library Settings','default_price_list')
# 	get_cust = frappe.db.get_value('Customer', {'employee_id':doc.name}, ['employee_id'])
# 	print(":::::::get_cust:::::::::", get_cust, doc.name)
# 	if get_cust == doc.name:
# 		customer = frappe.db.get_list('Customer',filters={'customer_name': doc.name },fields=['customer_name'], as_list=True)
# 		print(":::::::customer:::::::::", customer)

# 		customer_group_name = frappe.db.get_list('Customer Group',filters={'customer_group_name': doc.name },fields=['customer_group_name'], as_list=True)
# 		print(":::::::customer_group_name:::::::::", customer_group_name)

# 		contact = frappe.db.get_list('Contact',filters={'first_name': doc.name },fields=['first_name'], as_list=True)
# 		cp = frappe.db.get_value('Customer Group', {'name': doc.custom_employment_type}, ['name'])

# 		print(":::::::cp:::::::::", cp)
# 		if not cp:
# 			new_cp = frappe.new_doc('Customer Group',customer_group_name)
# 			new_cp.customer_group_name = doc.employment_type
# 			new_cp.save()
# 		em = frappe.get_doc('Customer',customer)
# 		em.employee_id = doc.name
# 		em.customer_name = doc.employee_name
# 		em.customer_group = doc.customer_group
# 		em.gender = doc.gender
# 		em.salutation = doc.salutation
# 		em.customer_group = doc.employment_type
# 		em.tax_id = doc.pan_number
# 		em.territory = def_ter
# 		em.default_price_list = def_pr
# 		em.save()
# 		cust_cont = frappe.db.get_value('Customer', {'employee_id':doc.name}, ['customer_primary_contact'])
# 		if cust_cont:
# 			cust_cont_upd = frappe.get_doc('Contact', cust_cont)
# 			cust_cont_upd.email_ids = []
# 			cust_cont_upd.phone_nos = []
# 			cust_cont_upd.links= []
# 			cust_cont_upd.save()
# 			cust_cont_upd.first_name = doc.employee_name
# 			cust_cont_upd.append('email_ids',{
# 					'email_id': doc.personal_email,
# 					'is_primary': 1
# 					})
# 			cust_cont_upd.append('phone_nos',{
# 					'phone': doc.cell_number,
# 					'is_primary_phone': 1,
# 					'is_primary_mobile_no':1
# 					})
# 			cust_cont_upd.append('links',{
# 					'link_doctype': "Customer",
# 					'link_name': em.name
# 					})
# 			cust_cont_upd.save ()
# 		cg = frappe.get_doc('Customer',em.name)
# 		cg.customer_primary_contact = cust_cont_upd.name
# 		cg.save()
# 	else:
# 		cp = frappe.db.get_value('Customer Group', {'name': doc.custom_employment_type}, ['name'])
# 		if not cp:
# 			new_cp = frappe.new_doc('Customer Group')
# 			new_cp.customer_group_name = doc.custom_employment_type
# 			new_cp.save()
# 		em = frappe.new_doc('Customer')
# 		em.employee_id = doc.name
# 		em.customer_name = doc.employee_name
# 		em.gender = doc.gender
# 		em.salutation = doc.salutation
# 		em.customer_group = doc.custom_employment_type
# 		em.territory = def_ter
# 		em.default_price_list = def_pr	
# 		em.insert() 
# 		con = frappe.new_doc('Contact')
# 		con.first_name = doc.employee_name
# 		con.append('email_ids',{
# 				'email_id': doc.personal_email,
# 				'is_primary': 1
# 				})
# 		con.append('phone_nos',{
# 				'phone': doc.cell_number,
# 				'is_primary_phone': 1,
# 				'is_primary_mobile_no':1
# 				})
# 		con.append('links',{
# 				'link_doctype': "Customer",
# 				'link_name': doc.employee_name
# 				})
# 		con.insert()
# 		cg = frappe.get_doc('Customer',em.name)
# 		cg.customer_primary_contact = con.name
# 		cg.save()