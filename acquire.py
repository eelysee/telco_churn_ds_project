import os
import pandas as pd
from env import get_connection 


# imports all tables from telco_churn db on Codeup's SQL server.
# dropped '11' customers whose tenure was 0 as they havn't completed a month yet.
def get_telco_churn():
    filename = 'telco_churn.csv'
    
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    
    else:
        url = get_connection('telco_churn')
        query = '''

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
        WHERE tenure <> 0
        ;

        '''
        
        telco_churn = pd.read_sql(query,url)
        telco_churn.to_csv(filename, index = 0)
        return telco_churn
