// Copyright (c) 2024, Ketan Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Penalty Template', {
	before_save: function(frm) {
		frm.set_value('penalty_template_name', frm.doc.no_of_day_penalty_from +"-"+ frm.doc.no_of_day_penalty_to);
	}
});
