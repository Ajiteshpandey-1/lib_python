
# Q1. Display Unique Values
# Create a DataFrame with a City column and display all unique cities.
import pandas as pd
City = ["Bhopal", "Indore","Bhopal", "Delhi"]
df=pd.DataFrame({
    'City':City
})
print(df.drop_duplicates())






# Q2. Count Unique Values
# Find the number of unique cities in a DataFrame.

City = ["Bhopal", "Indore", "Bhopal", "Delhi"]
df=pd.DataFrame({
    'City':City
})
print(df.nunique())




# Q3. Value Counts

## Problem Statement
# Count occurrences of each city.
City = ["Bhopal", "Indore", "Bhopal", "Delhi"]
df=pd.DataFrame({
    'City':City
})
print(df.value_counts())




# Q4. Group By City

## Problem Statement
# Find average marks city-wise using groupby().
Marks=[80,90,70]
City = ["Bhopal", "Bhopal", "Delhi"]
df=pd.DataFrame({
    'City':City,
    'Marks':Marks
})
print(df.groupby('City')['Marks'].mean())



# Q5. Sort Values
## Problem Statement
# Sort students by Marks in ascending order.
Marks=[80,90,70]
City = ["Bhopal", "Bhopal", "Delhi"]
df=pd.DataFrame({
    'City':City,
    'Marks':Marks
})
print(df['Marks'].sort_values(ascending=True))


# Q6. Sort Values Descending
## Problem Statement
# Sort students by Marks in descending order.
Marks=[80,90,70]
City = ["Bhopal", "Bhopal", "Delhi"]
df=pd.DataFrame({
    'City':City,
    'Marks':Marks
})
print(df['Marks'].sort_values(ascending=False))



# Q7. Filter Records
# Display students having marks greater than 75.
Marks=[80,90,70]
City = ["Bhopal", "Bhopal", "Delhi"]
df=pd.DataFrame({
    'City':City,
    'Marks':Marks
})
print(df[df['Marks']>75])



# Q8. Multiple Conditions
##Display students whose marks are greater than 70 and age is greater than 20.
Marks=[80,90,70]
age=[30,14,25]
df=pd.DataFrame({
    'Marks':Marks,
    'age':age
})
print(df[(df['Marks']>75) & (df['age']>25)])



# Q9. Group By Department
df=pd.DataFrame({
    "Employee":['Ajitesh','Ajay','Akshat','Heer'],
    'Salary':[30000,50000,80000,120000],
    'Department':['HR','IT','IT','HR']
})
print(df.groupby('Department')['Salary'].sum())



# q10. 
df=pd.DataFrame({
    'name':['ajitesh','ajay','akshat','heer'],
    'age':[20,21,22,21],
    'city':['bhopal','hoshangabad','narsingpur','gujrat'],
    'marks':[100,80,87,78]
})
print(df['city'].unique())
print(df['city'].value_counts())
print(df[df['marks']>80])
print(df['marks'].sort_values())