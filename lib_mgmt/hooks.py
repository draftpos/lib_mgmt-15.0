from . import __version__ as app_version

app_name = "lib_mgmt"
app_title = "Library Management"
app_publisher = "Ketan Patel"
app_description = "Library Management"
app_email = "contact@solufy.in"
app_license = "MIT"

# Includes in <head>
# ------------------
fixtures = [{
    "doctype": "Custom Field",
        "filters": {
            "module": ["in", ["Library Management"]]
            }
    },
    {
    "doctype": "Property Setter",
        "filters": {
            "module": ["in", ["Library Management"]]
            }
    },
    {
    "doctype": "Custom DocPerm",
        "filters": {
            "role": ["in", ["Librarian"]]
            }
    },
    {
    "doctype": "Role",
        "filters": {
            "name": ["in", ["Librarian"]]
            }
    },
    {
    "doctype": "Role Profile",
        "filters": {
            "name": ["in", ["Librarian"]]
            }
    }
]

# include js, css files in header of desk.html
# app_include_css = "/assets/lib_mgmt/css/lib_mgmt.css"
# app_include_js = "/assets/lib_mgmt/js/lib_mgmt.js"

# include js, css files in header of web template
# web_include_css = "/assets/lib_mgmt/css/lib_mgmt.css"
# web_include_js = "/assets/lib_mgmt/js/lib_mgmt.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lib_mgmt/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
			"Member" : "public/js/member.js",
			"Item" : "public/js/item.js",
			"Sales Invoice" : "public/js/sales_invoice.js",
			"Membership" : "public/js/membership.js"
		}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "lib_mgmt.utils.jinja_methods",
#	"filters": "lib_mgmt.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "lib_mgmt.install.before_install"
# after_install = "lib_mgmt.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "lib_mgmt.uninstall.before_uninstall"
# after_uninstall = "lib_mgmt.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lib_mgmt.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

doc_events = {
	# "Employee": {
	# 	"on_update": "lib_mgmt.public.py.employee.get_employee"
	# },
	"Membership": {
		"on_update": "lib_mgmt.public.py.membership.get_membership"
	},
	"Customer": {
		"on_update": "lib_mgmt.public.py.customer.get_member"
	},
	"Library Settings": {
		"on_update": "lib_mgmt.public.py.library_settings.lib_set"
	},
	"Sales Invoice": {
		"before_save":[
		"lib_mgmt.public.py.sales_invoice.get_penalty",
		],
		"on_submit":[
		"lib_mgmt.public.py.sales_invoice.penalty_create",
		"lib_mgmt.public.py.sales_invoice.allow_books"
		]
	},
	"Membership Type":{
		"before_save":[
		"lib_mgmt.public.py.membership_type.pricing_list"
		]
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"lib_mgmt.tasks.all"
#	],
#	"daily": [
#		"lib_mgmt.tasks.daily"
#	],
#	"hourly": [
#		"lib_mgmt.tasks.hourly"
#	],
#	"weekly": [
#		"lib_mgmt.tasks.weekly"
#	],
#	"monthly": [
#		"lib_mgmt.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "lib_mgmt.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "lib_mgmt.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "lib_mgmt.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["lib_mgmt.utils.before_request"]
# after_request = ["lib_mgmt.utils.after_request"]

# Job Events
# ----------
# before_job = ["lib_mgmt.utils.before_job"]
# after_job = ["lib_mgmt.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"lib_mgmt.auth.validate"
# ]
