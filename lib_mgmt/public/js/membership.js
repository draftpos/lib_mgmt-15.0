frappe.ui.form.on('Membership', {
	duration_of_membership:function(frm) {
		if(frm.doc.duration_of_membership == 'Monthly'){
			frm.set_value("to_date", frappe.datetime.add_months(frm.doc.from_date, 1));
		}else if(frm.doc.duration_of_membership == 'Six Month'){
			frm.set_value("to_date", frappe.datetime.add_months(frm.doc.from_date, 6));
		}else if(frm.doc.duration_of_membership == 'Yearly'){
			frm.set_value("to_date", frappe.datetime.add_months(frm.doc.from_date, 12));
		}else{
			frappe.throw("Please Select Atleast One Option")
		}
	},
	from_date:function(frm){
		frm.trigger('duration_of_membership')
	}	
});