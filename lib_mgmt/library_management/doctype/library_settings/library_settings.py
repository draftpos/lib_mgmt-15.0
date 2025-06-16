# Copyright (c) 2024, Ketan Patel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class LibrarySettings(Document):
	def on_update(doc):
		s_spl = frappe.db.get_single_value('Selling Settings', 'selling_price_list')
		s_dt = frappe.db.get_single_value('Selling Settings', 'territory')

		ss = frappe.get_doc("Selling Settings")
		if not s_spl:
			ss.selling_price_list = frappe.db.get_single_value('Library Settings', 'default_price_list')
			ss.save()

		if not s_dt:
			ss.territory = frappe.db.get_single_value('Library Settings', 'default_territory')
			ss.save()