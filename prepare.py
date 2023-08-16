
# SQL code for all churn data
'''

SELECT *
FROM customers
LEFT JOIN contract_types ON customers.contract_type_id = contract_types.contract_type_id
LEFT JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id
LEFT JOIN payment_types ON customers.payment_type_id = payment_types.payment_type_id
LEFT JOIN customer_churn ON customers.customer_id = customer_churn.customer_id
LEFT JOIN customer_contracts ON customers.customer_id = customer_contracts.customer_id
LEFT JOIN customer_details ON customers.customer_id = customer_details.customer_id
LEFT JOIN customer_payments ON customers.customer_id = customer_payments.customer_id
LEFT JOIN customer_signups ON customers.customer_id = customer_signups.customer_id
LEFT JOIN customer_subscriptions ON customers.customer_id = customer_subscriptions.customer_id
;

'''