
import pandas as pd
from sklearn.model_selection import train_test_split

# regex for dropping dupe columns
import re

seed = 55


def prep_telco(telco):
    # drops all duplicate columns
    for i in telco.columns:
        if re.search(r'\d$',i):
            telco.drop(i, axis = 1, inplace = True)
            
    # drops redundant columns in favor of their numerical or boolean counterparts. 
    # drop churn month becuse all values are the same.
    telco.drop(columns = ['payment_type', 'customer_id', 'contract_type', 'internet_service_type', 
                          'churn_month', 'signup_date'], inplace = True)
    
    # rename's columns for to be more explicit or simple
    telco.rename(columns = {'senior_citizen': 'senior', 'internet_service_type_id' :'internet_type', 
                     'contract_type_id': 'contract_type'} , inplace = True)
    
    # adds a feature which is the sum of all additional services that customer has. 
    telco['add_ons'] = (
        (telco.phone_service == 'Yes').astype(int) + 
        (telco.multiple_lines == 'Yes').astype(int)+ 
        (telco.online_security == 'Yes').astype(int) + 
        (telco.multiple_lines == 'Yes').astype(int) + 
        (telco.online_backup == 'Yes').astype(int) + 
        (telco.tech_support == 'Yes').astype(int) + 
        (telco.streaming_tv == 'Yes').astype(int) + 
        (telco.streaming_movies == 'Yes').astype(int)
    )
    
    return telco


# feature == target feature in quotes
def train_val_test(df, feature, seed = 55):

    train, val_test = train_test_split(df, train_size = 0.7,
                                       random_state = seed,
                                       stratify = df[feature])
    
    val, test = train_test_split(val_test, train_size = 0.5,
                                 random_state = seed,
                                 stratify = val_test[feature])
    
    return train, val, test