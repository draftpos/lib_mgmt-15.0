// Copyright (c) 2024, Ketan Patel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Library Settings', {
	refresh: function(frm) {
		frm.set_query('default_terms_and_conditions', () => {
        	return {
            	filters: {
                	selling: 1
            	}
        	}
    	});
		frm.set_query('penalty_charge_item', () => {
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
});
