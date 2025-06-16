frappe.ui.form.on('Item', {
	is_book_item(frm) {
		change_label(frm);
	},
	refresh(frm) {
		change_label(frm);
	}
});

function change_label(frm) {
    if (frm.doc.is_book_item == 1) {
        frm.set_value('has_serial_no', 1);
        frm.set_df_property("item_name", "label", "Book Name");
        frm.set_df_property("item_code", "label", "Book Code");
        frm.set_df_property("item_group", "label", "Book Group");
        frm.set_df_property("brand", "label", "Book Brand");
    } else {
        frm.set_value('has_serial_no', 0);
        frm.set_df_property("item_name", "label", "Item Name");
        frm.set_df_property("item_code", "label", "Item Code");
        frm.set_df_property("item_group", "label", "Item Group");
        frm.set_df_property("brand", "label", "Brand");
    }
}