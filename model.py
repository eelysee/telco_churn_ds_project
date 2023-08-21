# graphing explore part
import matplotlib.pyplot as plt
import seaborn as sns

#Statistics part
import pandas as pd
import numpy as np

from sklearn.metrics import confusion_matrix
from scipy.stats import mannwhitneyu
from scipy.stats import chi2_contingency


# Explore portion
# For graphs

#just plug in df. Can be used on train, or val
# Shoudl be used in definition and conclusion
def churn_pie(dataframe):
    counts = dataframe.churn.value_counts()

    plt.figure(figsize=(8, 6))
    counts.plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title("Churn Distribution")
    plt.ylabel("")
    plt.show()
    
    
def churn_scatter_plot(dataframe):
    plt.figure(figsize=(12, 6))

    # Scatter plot for customers who churned
    churned = dataframe[dataframe['churn'] == 'Yes']
    plt.scatter(churned['monthly_charges'], churned['total_charges'], color='red', label='Churned', alpha=0.5)

    # Scatter plot for customers who did not churn
    not_churned = dataframe[dataframe['churn'] == 'No']
    plt.scatter(not_churned['monthly_charges'], not_churned['total_charges'], color='green', label='Not Churned', alpha=0.5)

    # Plot settings
    plt.title("Total Charges vs Monthly Charges by Churn Status")
    plt.xlabel("Monthly Charges")
    plt.ylabel("Total Charges")
    plt.legend()
    plt.grid(True)
    plt.show()

    
def churn_line_plot(dataframe):
    plt.figure(figsize=(12, 6))

    # Group data by tenure and churn status, then compute the mean of total_charges
    avg_charges = dataframe.groupby(['tenure', 'churn'])['total_charges'].mean().reset_index()

    # Plot line chart
    sns.lineplot(x='tenure', y='total_charges', hue='churn', data=avg_charges)
    
    # Title & Labels
    plt.title('Average Total Charges Over Tenure by Churn Status')
    plt.xlabel('Tenure (Months)')
    plt.ylabel('Average Total Charges')
    plt.legend(title='Churn Status')
    
    plt.tight_layout()
    plt.grid(axis='y')
    plt.show()
    

   
# Statistical portion



    
#takes in df and two columns and runs a man whitney. Target colum shoudl be second.
# churn is always second. Use small function for comparing correlation.
# columns must be in ''
# df must be it's own seperate tuple
def mann_whitney_test(df, feature_col, target_col):
    
    # Split data into two groups
    group1 = df[df[target_col] == df[target_col].unique()[0]][feature_col]
    group2 = df[df[target_col] == df[target_col].unique()[1]][feature_col]

    # Perform Mann-Whitney U Test
    stat, p_value = mannwhitneyu(group1, group2)

    print(f"U-statistic: {stat}")
    print(f"P-value: {p_value}")

    if p_value < 0.05:
        print(f"Reject the null hypothesis: {feature_col} has an effect on {target_col}.")
    else:
        print(f"Fail to reject the null hypothesis: No significant evidence to suggest that {feature_col} affects {target_col}.")

        
# Function to test if differnt addons correlate to eachother
def mann_whitney_test2(feature1, feature2):
    stat, p_value = mannwhitneyu(feature1, feature2)

#chi^2 test    
def chi_squared_test(df, column1, column2):

    contingency_table = pd.crosstab(df[column1], df[column2])
    
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    
    print(f"Chi-Squared Value = {chi2}")
    print(f"P-value = {p}")
    print(f"Degrees of Freedom = {dof}")
    print("Expected Frequencies Table:")
    print(expected)
    
    if p < 0.05:
        print(f"\nThe variables {column1} and {column2} are dependent (reject H_0).")
    else:
        print(f"\nThe variables {column1} and {column2} are independent (fail to reject H_0).")
    
    return chi2, p, dof, expected
    
   
    
# Modeling Portion

# Theometrics but it accepts teh columns instead and gives out confusiotn matrix
def theometrics2(y_true, y_pred):
    # Create a confusion matrix
    matrix = confusion_matrix(y_true, y_pred)
    TP = matrix[1, 1]
    TN = matrix[0, 0]
    FP = matrix[0, 1]
    FN = matrix[1, 0]
    
    # Display confusion matrix
    df_matrix = pd.DataFrame(matrix, 
                             columns=['Predicted Negative', 'Predicted Positive'], 
                             index=['Actual Negative', 'Actual Positive'])
    print("Confusion Matrix:")
    print(df_matrix)
    print("\n")
    
    # Calculate metrics
    accuracy = (TP + TN) / (TP + TN + FP + FN)
    recall = TP / (TP + FN)
    true_positive_rate = TP / (TP + FN)
    false_positive_rate = FP / (FP + TN)
    true_negative_rate = TN / (TN + FP)
    false_negative_rate = FN / (FN + TP)
    precision = TP / (TP + FP)
    f1_score = 2 * (precision * recall) / (precision + recall)
    support = TP + FN
    data = {
        'Metric': ['Accuracy', 'Recall', 'True Positive Rate', 'False Positive Rate', 'True Negative Rate', 'False Negative Rate', 'Precision', 'F1-Score', 'Support'],
        'Value': [accuracy, recall, true_positive_rate, false_positive_rate, true_negative_rate, false_negative_rate, precision, f1_score, support]
    }
    theometrics2 = pd.DataFrame(data)
    return theometrics2

