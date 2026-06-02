import pandas as pd
import matplotlib.pyplot as plt
# ----------------------------
# Loading Data
# ----------------------------
#loading the student_budget data from a csv file
df_student_budget= pd.read_csv("student_budget.csv")  
#showing the student_budget data
print(df_student_budget)
#----------------------------
#cleaning data
#----------------------------

#checking for duplicates
print(df_student_budget[df_student_budget.duplicated()])

#counting the number of duplicates
print(df_student_budget.duplicated().sum())



#removing duplicates
df_student_budget = df_student_budget.drop_duplicates()

#verifying the duplicates are removed
print(df_student_budget.duplicated().sum())
#Or
#verifying by unique values
print(df_student_budget['student_id'].nunique())
print(df_student_budget['student_id'].shape[0])

#null values in the dataset
print(df_student_budget.isnull().sum())

#filling null values in scholarship with 0
df_student_budget['scholarship'] = df_student_budget['scholarship'].fillna(0)

#checking for negative values in monthly_income
print(df_student_budget[df_student_budget['monthly_income'] < 0])

#standardizing program names and country names to title case
df_student_budget['country'] = df_student_budget['country'].str.title()
df_student_budget['program'] = df_student_budget['program'].str.title()

#total expenses
df_student_budget['total_expenses'] = df_student_budget['rent'] + df_student_budget['food'] + df_student_budget['transport'] + df_student_budget['entertainment'] + df_student_budget['other_expenses']
print(df_student_budget)

#savings
df_student_budget['savings'] = df_student_budget['monthly_income'] - df_student_budget['total_expenses']
print(df_student_budget)

#highest savings
print(df_student_budget[df_student_budget['savings'] == df_student_budget['savings'].max()])

#top 5 students with the highest savings
top_5_savings = df_student_budget.nlargest(5, 'savings')
print(top_5_savings)

#average savings by program
avg_savings_by_program = df_student_budget.groupby('program')['savings'].mean()
print(avg_savings_by_program)
sorted_avg_saving_by_p = avg_savings_by_program.sort_values()


#highest average savings by program
print(avg_savings_by_program[avg_savings_by_program == avg_savings_by_program.max()])

#average saving by country
avg_saving_by_country = df_student_budget.groupby('country')['savings'].mean()
print(avg_saving_by_country)
sorted_avg_saving_by_c = avg_saving_by_country.sort_values()

#highest average income by program
avg_income_by_program = df_student_budget.groupby('program')['monthly_income'].mean()
print(avg_income_by_program[avg_income_by_program==avg_income_by_program.max()])

#highest average rent by country
avg_rent_by_country = df_student_budget.groupby('country')['rent'].mean()
print(avg_rent_by_country[avg_rent_by_country==avg_rent_by_country.max()])

#top 5 spenders
top_5_spenders = df_student_budget['total_expenses'].sort_values(ascending=False,).head(5)
print(top_5_spenders)

#-----------------
#plotting(subplot)
plt.figure(figsize=(12,8))
plt.subplot(1,3,1)
sorted_avg_saving_by_p.plot(kind= 'bar')
plt.title('student savings per program')
plt.xlabel('Program')
plt.ylabel('Students savings')
plt.xticks(rotation=90)
plt.subplot(1,3,2)
sorted_avg_saving_by_c.plot(kind='bar')
plt.title('student savings per country')
plt.xlabel('Country')
plt.ylabel('Student savings')
plt.xticks(rotation=90)
plt.subplot(1,3,3)
df_student_budget['savings'].plot(kind='hist', bins=10)
plt.title('saving distribution')
plt.xlabel('Student savings')
plt.ylabel('frequency')
plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()


