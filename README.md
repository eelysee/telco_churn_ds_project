# Telco Churn Data Science Project

# Project Description

Telco Churn is a dataset utilized for training in data analytics, encompassing a variety of machine learning techniques and best practices.

The data set is customer information from Telco, z ficticious telecommunications company, for the month of January 2022. The data is dated 01/31/2022.

This project aims to demonstrate proficency in the full data science pipeline including but not limited to:
 
* Data preperation
* Exploratory analysis
* Data preprocessing
* Feature engineering
* Statistical analysis
* Predictive modeling
* Model evaluation
* Business acumen
* Effective communication off all findings and insights 

# Project Goal

* Find drivers for customer churn at Telco. Why are customers churning?
* Construct a ML classification model that accurately predicts customer churn
* Present your process and findings to the lead data scientist

# Steps to Reproduce
1) Clone this repo.
2) Acquire the data from Codeup's SQL server.
3) Put the data in the file containing the cloned repo.
4) Run notebook.

# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|add_ons| Integer. The count of additional services a customer has subscribed to.|
|churn| Bool. Indicates if a customer left the service or stayed.|
|contract_type| Categorical. Describes the duration and terms of the customer's contract. Month-to-month - 1, Two year- 3, One year-2|
|dependents| Bool. Indicates if the customer has any dependents.|
|device_protection| Bool. Specifies if the customer has enrolled in a device protection service.|
|gender| Categorical. The gender of the customer.|
|internet_type| Categorical. Describes the type of internet service the customer is using. Fiber optic-2
DSL-1|
|monthly_charges| Numeric. The amount charged to the customer every month.|
|multiple_lines| Categorical. Specifies if the customer has multiple phone lines or none at all.|
|online_backup| Bool. Denotes if the customer has an online backup service.|
|online_security| Bool. Indicates if the customer has an online security service.|
|paperless_billing| Bool. Specifies if the customer has chosen paperless billing.|
|partner| Bool. Indicates if the customer has a partner.|
|payment_type_id| Categorical/Numeric. An identifier representing the payment method chosen by the customer. Mailed check-2,
Bank transfer (automatic)- 3, Credit card (automatic)-4|
|phone_service| Bool. Indicates if the customer has subscribed to a phone service.|
|senior| Bool. Denotes if the customer is classified as a senior citizen.|
|streaming_movies| Bool. Shows if the customer uses the service for streaming movies.|
|streaming_tv| Bool. Shows if the customer uses the service for streaming TV.|
|tech_support| Bool. Specifies if the customer has a tech support service.|
|tenure| Numeric. The total number of months the customer has used the service.|
|total_charges| Numeric. The cumulative amount charged to the customer for the duration of their subscription.|

# Initial Thoughts and Questions
 
What effect does tenure have on churn?




I think different combinations of addons could be a strong predictor of churn.
 
# The Plan
 
* Aquire data from Codeup
 
* Prepare data
    * Drop duplicate columns colums 
    * Drop redundant columns in favor of their numerical or boolean counterparts. Drop churn month.
        * payment_type
        * customer_id
        * contract_type
        * internet_service_type
        * churn_month
        * signup_date
    * Create Engineered columns from existing data
       * add_ons
 
* Explore data in search of drivers of upsets
   * Answer the following initial questions
        * What effect does tenure have on churn?
        * What effect does total charges have on churn?
        * How do differnt add-ons effect churn?
        * Is costomer demographic a predictor of churn?
      
* Develop a Model to predict if a customer will churn or not.
   * Use drivers identified in explore to build predictive models of different types
   * Evaluate models on train and validate data
   * Select the best model based on highest accuracy
   * Evaluate the best model on test data
 
* Draw conclusions

# Takeaways and Conclusions
* 
* 

# Recommendations
* 




Final takeaway

Explain the cosst of churn. earlier
how many people are churngin per month

explain what the predictions and cost savings will be with reduciotn so they can know the budget for such actions
need to come up with the average of monthly expenses by customer.
-- either caluculate teh actual nuber of people churned.
-- the average cost of money saved per month means the total of all churned
-- look at that number of saved money compounded with growth over a year
--- woudl need to add on the base of tenure zero per month - the new churn amounts if we are able to capture them all
-- a good place to add some distributions possibly.
-- when figuring out how much the budget to make changes or how much discount can be given

We shoudl touch on reservatoin price.

I suggest we do another study on reservatoin price to perhaps raise the cost of the dsl as it is our best feartures. If it does meat 