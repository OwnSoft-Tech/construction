def pages(request):
    Registration = {
    "all_registration_pages": [
        "add_customers",
        "manage_customers",
        "add_vendor",
        "manage_vendor",
        "add_estate_agents",
        "manage_estate_agents",
        "add_product_types",
        "manage_product_types",
        "add_products",
        "manage_products",
        "add_taxes",
        "manage_taxes",
        "add_bank_accounts",
        "manage_bank_accounts",
        "add_assets",
        "manage_assets",
        "add_users",
        "manage_users",
        "add_expense_types",
        "manage_expense_types",
        "add_warehouses",
        "manage_warehouses",
    ],
    "customers": [
        "add_customers",
        "manage_customers"
    ],
    "vendor": [
        "add_vendor",
        "manage_vendor"
    ],
    "estateAgents": [
        "add_estate_agents",
        "manage_estate_agents"
    ],
    "producttypes": [
        "add_product_types",
        "manage_product_types"
    ],
    "products": [
        "add_products",
        "manage_products"
    ],
    "taxes": [
        "add_taxes",
        "manage_taxes"
    ],
    "bankacounts": [
        "add_bank_accounts",
        "manage_bank_accounts"
    ],
    "assets": [
        "add_assets",
        "manage_assets"
    ],
    "users": [
        "add_users",
        "manage_users"
    ],
    "expensetypes": [
        "add_expense_types",
        "manage_expense_types"
    ],
    "warehouses": [
        "add_warehouses",
        "manage_warehouses"
    ],
    "all_account_pages": [
        "add_bank_deposit_voucher",
        "add_debit_notes",
        "add_expense_voucher",
        "add_journal_voucher",
        "add_opening_voucher",
        "add_payment_voucher",
        "add_receipt_voucher",
        "chart_of_accounts",
        "manage_bank_deposit_voucher",
        "manage_debit_notes",
        "manage_expense_voucher",
        "manage_journal_voucher",
        "manage_opening_voucher",
        "manage_payment_voucher",
        "manage_receipt_voucher",
    ],
    "PaymentVouchers": [
        "manage_payment_voucher",
        "add_payment_voucher"
    ],
    "ExpenseVouchers": [
        "add_expense_voucher",
        "manage_expense_voucher"
    ],
    "ReceiptVouchers": [
        "add_receipt_voucher",
        "manage_receipt_voucher"
    ],
    "OpeningVouchers": [
        "add_opening_voucher",
        "manage_opening_voucher"
    ],
    "JournelVouchers": [
        "add_journal_voucher",
        "manage_journal_voucher"
    ],
    "DebitNotes": [
        "add_debit_notes",
        "manage_debit_notes"
    ],
    "BankDeposits": [
        "add_bank_deposit_voucher",
        "manage_bank_deposit_voucher"
    ],
    "ChartOfAccounts": [
        "chart_of_accounts"
    ],

    "all_sales_pages":[
        "add_additional_charges",
        "manage_additional_charges",
        "add_agent_commission",
        "manage_agent_commission",
        "add_property_buy_back",
        "manage_property_buy_back",
        "add_installment_plan",
        "manage_installment_plan",
        "add_installment_plan_B",
        "manage_installment_plan_B",
        "generate_properties",
        "manage_properties",
        "add_property_cancellation",
        "manage_property_cancellation",
        "add_property_transfer",
        "manage_property_transfer",
        "add_property_merger",
        "manage_property_merger",
        "add_property_sale",
        "manage_property_sale",
        "add_property_surcharge",
        "manage_property_surcharge",
        "add_surcharge_waiver",
        "manage_surcharge_waiver",
        "master_delete_property_sales",
        "upgrade_property_prices"
    ],
    "additionalcharges": [
        "add_additional_charges",
        "manage_additional_charges"
    ],
    "agentcommission": [
        "add_agent_commission",
        "manage_agent_commission"
    ],
    "propertybuyback": [
        "add_property_buy_back",
        "manage_property_buy_back"
    ],
    "installmentplan": [
        "add_installment_plan",
        "manage_installment_plan"
    ],
    "installmentplanB": [
        "add_installment_plan_B",
        "manage_installment_plan_B"
    ],
    "generateproperties": [
        "generate_properties",
        "manage_properties"
    ],
    "propertycancellation": [
        "add_property_cancellation",
        "manage_property_cancellation"
    ],
    "propertytransfer": [
        "add_property_transfer",
        "manage_property_transfer"
    ],
    "propertymerger": [
        "add_property_merger",
        "manage_property_merger"
    ],
    "propertysale": [
        "add_property_sale",
        "manage_property_sale"
    ],
    "propertysurcharge": [
        "add_property_surcharge",
        "manage_property_surcharge"
    ],
    "surchargewaiver": [
        "add_surcharge_waiver",
        "manage_surcharge_waiver"
    ],
    "deletepropertysales": [
        "master_delete_property_sales",
    ],
    "upgradepropertyprices": [
        "upgrade_property_prices"
    ],
    "all_construction_pages":[
        "add_construction_note",
        "construction_stage_chart",
        "manage_construction_note"
    ],
    "constructionnotes": [
        "add_construction_note",
        "manage_construction_note"
    ],
    "constructionstagechart": [
        "construction_stage_chart"
    ],

    "all_hr_pages": [
        "add_employee_attendance",
        "manage_employee_attendance",
        "add_employee_note",
        "manage_employee_note",
        "add_employee",
        "manage_employee",
        "add_employee_loan_disbursement",
        "manage_loan_disbursement",
        "add_employee_loan_repayment_receipt",
        "manage_loan_receipt",
        "add_salary_head",
        "manage_salary_head",
        "add_salary_slip",
        "manage_salary_slips",
        "add_salary_structure",
        "manage_salary_structure",
        "generate_pay_roll"
    ],
    "employeeattendance": [
        "add_employee_attendance",
        "manage_employee_attendance"
    ],
    "employeenote": [
        "add_employee_note",
        "manage_employee_note"
    ],
    "employees": [
        "add_employee",
        "manage_employee"
    ],
    "loandisbursements": [
        "add_employee_loan_disbursement",
        "manage_loan_disbursement"
    ],
    "loanreceipts": [
        "add_employee_loan_payment_receipt",
        "manage_loan_receipt"
    ],
    "salaryheads": [
        "add_salary_head",
        "manage_salary_head"
    ],
    "salaryslips": [
        "add_salary_slip",
        "manage_salary_slips"
    ],
    "salarystructures": [
        "add_salary_structure",
        "manage_salary_structure"
    ],
    "generatepayroll": [
        "generate_pay_roll"
    ],

    "all_reports_pages":[
        "account_ledger",
        "account_payables",
        "account_receivables",
        "balance_sheet_summary",
        "balance_sheet",
        "bank_ledger",
        "customer_ledger",
        "employee_commission_ledger",
        "employee_ledger",
        "estate_agent_ledger",
        "general_ledger",
        "profit_loss_statement",
        "trial_balance",
        "vendor_ledger",
        "construction_ledger",
        "delayed_construction_stages",
        "breakage_report",
        "inventory_consumed_value_wise",
        "inventory_consumption",
        "inventory_in_hand",
        "inventory_ledger",
        "inventory_procured_value_wise",
        "inventory_report",
        "inventory_value_wise",
        "batch_analysis_report",
        "pending_requisition_orders",
        "pending_stock_for_purch_order",
        "previous_requisition_actions",
        "product_wise_purchase",
        "requisition_order_status",
        "vendor_wise_purchase",
        "customer_properties_summary",
        "due_installments",
        "late_installments",
        "outstanding_additional_charges",
        "outstanding_installments",
        "payment_collection",
        "property_wise_due",
        "property_wise_outstandings",
        "sales_property_statement",
        "sales_with_full_payment"
    ],
    "accounts": [
        "account_ledger",
        "account_payables",
        "account_receivables",
        "balance_sheet_summary",
        "balance_sheet",
        "bank_ledger",
        "customer_ledger",
        "employee_commission_ledger",
        "employee_ledger",
        "estate_agent_ledger",
        "general_ledger",
        "profit_loss_statement",
        "trial_balance",
        "vendor_ledger"
    ],
    "construction": [
        "construction_ledger",
        "delayed_construction_stages"
    ],
    "inventory": [
        "breakage_report",
        "inventory_consumed_value_wise",
        "inventory_consumption",
        "inventory_in_hand",
        "inventory_ledger",
        "inventory_procured_value_wise",
        "inventory_report",
        "inventory_value_wise"
    ],
    "purchases": [
        "batch_analysis_report",
        "pending_requisition_orders",
        "pending_stock_for_purch_order",
        "previous_requisition_actions",
        "product_wise_purchase",
        "requisition_order_status",
        "vendor_wise_purchase"
    ],
    "sales": [
        "customer_properties_summary",
        "due_installments",
        "late_installments",
        "outstanding_additional_charges",
        "outstanding_installments",
        "payment_collection",
        "property_wise_due",
        "property_wise_outstandings",
        "sales_property_statement",
        "sales_with_full_payment"
    ],

    "all_sms_pages": [
        "generate_sms",
        "manage_sms",
        "sms_settings"
    ],
    "sms": [
        "generate_sms",
        "manage_sms",
        "sms_settings"
    ],

    "all_purchases_pages": [
        'add_inventory_out_voucher',
        'manage_inventory_out_voucher',
        'add_purchase_order_cancel',
        'manage_purchase_order_cancel',
        'add_purchase_order',
        'manage_purchase_orders',
        'add_purchase_return',
        'manage_purchase_returns',
        'add_requisition_approval',
        'manage_requisition_approval',
        'add_requisition_order',
        'manage_requisition_order',
        'add_stock_receiving_voucher',
        'manage_stock_voucher',
        "requisition_approval_action_list",
    ],
    "inventoryoutvoucher": [
        'add_inventory_out_voucher',
        'manage_inventory_out_voucher'
    ],
    "purchaseordercancel": [
        'add_purchase_order_cancel',
        'manage_purchase_order_cancel'
    ],
    "purchaseorder": [
        'add_purchase_order',
        'manage_purchase_orders'
    ],
    "purchasereturn": [
        'add_purchase_return',
        'manage_purchase_returns'
    ],
    "requisitionapproval": [
        'add_requisition_approval',
        'manage_requisition_approval'
    ],
    "requisitionorder": [
        'add_requisition_order',
        'manage_requisition_order'
    ],
    "stockreceivingvoucher": [
        'add_stock_receiving_voucher',
        'manage_stock_voucher'
    ],
    "requisitionapprovalactionlist": [
        "requisition_approval_action_list"
    ],
}
    return {"pages": Registration}
