frappe.ui.form.on('Member', {
	refresh: function(frm) {
		frm.add_custom_button(__("Membership"), function() {
   	 	frappe.new_doc("Membership", {'name': ""},
        	doc => {
            	doc.member = frm.doc.name;
            	doc.membership_type = frm.doc.membership_type;
        	});
   		});
	}
});

