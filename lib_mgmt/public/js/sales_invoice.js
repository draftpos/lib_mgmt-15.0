frappe.ui.form.on('Sales Invoice', {
	refresh:function(frm) {        
		if(!frm.doc.is_penalty && !frm.doc.is_return){
			var ls =  frappe.db.get_single_value('Library Settings', 'default_terms_and_conditions').then((value) => {
				frm.set_value('tc_name',value)
  			});
			var ls =  frappe.db.get_single_value('Library Settings', 'allow_return_day').then((value) => { 
				var date = new Date(frm.doc.posting_date);
				date.setDate(date.getDate() + value);
				frm.set_value('return_date',new Date(date).toJSON().slice(0,10))
  			});
		}
	},
	posting_date: function(frm) {
		frm.trigger('refresh');
	},
	return_date: function(frm) {
		if(!frm.doc.is_penalty && !frm.doc.is_return){
			var ls =  frappe.db.get_single_value('Library Settings', 'allow_return_day').then((value) => {
				var sdc = frappe.datetime.get_day_diff(frm.doc.return_date,frm.doc.posting_date)
				if (sdc > value) {
					frappe.throw("You Cannot Select Return-Date More Than "+ value + " Days From Date: "+ frm.doc.posting_date);
				}
				if (sdc < 0) {
					frappe.throw("You Cannot Select Return Date Before Posting Date");
				}
  			});
		}
	}
})

frappe.ui.form.on('Sales Invoice', {
	before_save:function(frm) {
		var today = new Date();
		if(frm.doc.is_return == 1){
			var pen_day = frappe.datetime.get_day_diff(today,frm.doc.return_date)
			frm.set_value('overdue_penalty',pen_day)
		}	
	}
});

frappe.ui.form.on('Sales Invoice', {
	after_save:function(frm) {
		if(frm.doc.is_penalty == 1){
			frm.set_value('ignore_pricing_rule',1)
			frm.set_query("item_code", "items", function(doc, cdt, cdn) {
				var row = locals[cdt][cdn];
	            return {
	                "filters": {
	                	'is_stock_item': 0,
						'is_book_item':0,
						'has_variants':0,
						'include_item_in_manufacturing': 0
	            	}
	            }
	        })
		}
	}
});		