import re

# SQL code for all churn data

def prep_telco(telco):
    # drops all duplicate columns
    for i in telco.columns:
        if re.search(r'\d$',i):
            telco.drop(i, axis = 1, inplace = True)
            
    # drops redundant columns in favor of their numerical or boolean counterparts. 
    # drop churn month becuse all values are the same.
    telco.drop(columns = ['payment_type', 'customer_id', 'contract_type', 'internet_service_type', 
                          'churn_month', 'signup_date'], inplace = True)
    
    telco.rename(columns = {'senior_citizen': 'senior', 'internet_service_type_id' :'internet_type', 
                     'contract_type_id': 'contract_type'} , inplace = True)
    return telco