# Telco Churn Data Science Project

# Project Description

Telco Churn is a data set used for training on data analytics and numerous machine learnig and practices.

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

# Data Dictionary

| Feature | Definition |
|:--------|:-----------|
|add_ons| Integer. of how many optional services a customer has.|
|churn| Bool|
|White Rating| Rating of the player moving the white pieces using the Glicko-2 rating method for games played on Lichess|
|Black Rating| Rating of the player moving the white pieces using the Glicko-2 rating method for games played on Lichess|
|Rating Difference| The difference in rating between the players in the game|
|Game Rating| The average rating of the two players in the game|
|Lower Rated White| True or False, The lower rated player is moving the white pieces|
|Opening Name| The name of the opening played in the game|
|Time Control Group| The amount of time allotted to each player to make their moves, **Standard** (60 min or more), **Rapid** (30 - 15 min), **Blitz** (5 - 3 min), or **Bullet** (2 or less), **Other** (any other time limit)|
|Upset (Target)| True or False, The lower rated player won the game|
|Additional Features|Encoded and values for categorical data and scaled versions continuous data|

# Steps to Reproduce
1) Clone this repo.
2) Acquire the data from [Kaggle](https://www.kaggle.com/datasnaek/chess)
3) Put the data in the file containing the cloned repo.
4) Run notebook.

# Takeaways and Conclusions
* Upsets occur in 1/3 of games
* In games where the lower rated player moves first there is a 4% greater chance of an upset

# Recommendations
* To increase the skill intensity of a game add to the length of time players are able to consider their moves


README
Your README should contain all of the following elements:

Title Gives the name of your project
Project Description Describes what your project is and why it is important
Project Goal Clearly states what your project sets out to do and how the information gained can be applied to the real world
Initial Hypotheses Initial questions used to focus your project
Project Plan Guides the reader through the different stages of the pipeline as they relate to your project
Data Dictionary Gives a definition for each of the features used in your report and the units they are measured in, if applicable


Dropped all tenure 
payment_type               payment_type_id
Electronic check           1                  
Mailed check               2                  
Bank transfer (automatic)  3                  
Credit card (automatic)    4                  

contract_type   contract_type_id
Month-to-month  1                   
Two year        3                   
One year        2            

internet_service_type  internet_service_type_id
Fiber optic            2                           
DSL                    1                           



Churn Month == 2022-01-31
when churn == yes

Steps to Reproduce Gives instructions for reproducing your work. i.e. Running your notebook on someone else's computer.


Questions:
What effect does tenure have on churn?
What effect does total charges have on churn?
How do differnt add-ons effect churn?
Is costomer demographic a predictor of churn?

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