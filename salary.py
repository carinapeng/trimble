import pandas as pd

salaries = pd.read_csv('white_house_2017_salaries.csv')
# Print head of data
# print(salaries.head())
# Drop NA values
salaries = salaries.dropna()
# Convert column names to lowercase
salaries.columns=salaries.columns.str.lower()

salaries['salary'] = salaries['salary'].str.replace(',','')
salaries['salary'] = salaries['salary'].str.replace('$','')
salaries['salary'] = salaries['salary'].astype(float)

mean = salaries['salary'].mean()
mode = salaries['salary'].mode()
median = salaries['salary'].median()

