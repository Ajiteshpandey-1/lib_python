# Q1. Create a Student DataFrame
import pandas as pd
df=pd.DataFrame({
"Name":["Aman","Rahul","Neha","Priya","Ravi"],
"Age":[21,22,20,23,21],
"City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
"Marks":[85,72,91,68,95]
})
print(df)


# Q2. Display Selected Columns
# Using the DataFrame created in Question 1, display only the **Name** and **Marks** columns.
import pandas as pd
df=pd.DataFrame({
"Name":["Aman","Rahul","Neha","Priya","Ravi"],
"Age":[21,22,20,23,21],
"City":["Bhopal","Indore","Delhi","Bhopal","Indore"],
"Marks":[85,72,91,68,95]
})
print(df[['Name','Marks']])

# Q3. Filter Students
# Display only those students whose **Marks are greater than 75**.
print(df[df['Marks']>75])


# Q4. Sort by Marks
## Problem Statement
# Sort the DataFrame by **Marks** in descending order.
print(df['Marks'].sort_values(ascending=False))



# Q5. Average Marks by City
# Find the average Marks of each City using **groupby()**.
print(df.groupby('City')['Marks'].mean())


# Q6. Count Students by City
# Count the number of students in each City using **value_counts()**.
print(df['City'].value_counts())


# Q7. Create Result Column
# Create a new column named **Result**. If Marks are
# **40 or more**, store **Pass**, otherwise **Fail**.
df['result']='fail'
df.loc[df['Marks']>40,'result']='pass'
print(df)


# Q8. Remove Duplicate Rows
df=pd.DataFrame({
    'name':['aman','rahul','aman','neha'],
    'age':[21,22,21,20],
    'city':['bhopal','indore','bhopal','delhi'],
    'marks':[85,72,85,91]
})
print(df.drop_duplicates())


# Q9. Fill Missing Values
import numpy as np
df=pd.DataFrame({
    'Name':['aman','rahul','neha','priya'],
    'marks':[85,np.nan,91,np.nan]
})
df['marks']=(df['marks'].fillna(0))
print(df)



# q 10 
df=pd.DataFrame({
    'Name':['aman','rahul','neha','priya','ravi'],
    'marks':[85,72,91,68,95],
    'city':['bhopal','indore','delhi','bhopal','indore']
})
print(df[df['marks']>80])
print(df['marks'].sort_values())
print(df.groupby('city')['marks'].mean())