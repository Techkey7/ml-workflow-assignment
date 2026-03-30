Task 1: Label (Target Variable)

Label: flag for repeat purchases
 The outcome we are attempting to forecast—whether a customer makes a repeat purchase within 30 days (binary classification target)—is directly represented by this column.

Data Leakage Column: discount_used_on_repeat_order
 Including this value as an input feature would leak future information into the model and artificially inflate performance because it is only known after the repeat purchase takes place.


Task 2:

These two actions should be completed prior to training a Gradient Boosting model:

1. Analysis of Exploratory Data (EDA)

- EDA helps in understanding the distribution of variables, detecting outliers, and identifying relationships between features and the target variable.  
- It ensures that data quality issues are identified before model training.

Data Preprocessing (Cleaning + Feature Preparation)

- This step includes handling missing values, removing or treating outliers, encoding variables, and excluding leakage features.  
- Proper preprocessing ensures that the model learns meaningful patterns instead of noise or biased information.

 Summary

Before applying complex models like Gradient Boosting, it is essential to:
- Understand the dataset through EDA  
- Prepare clean and reliable features  

Skipping these steps can lead to overfitting and misleading model performance.