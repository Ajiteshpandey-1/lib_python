# ques 1
## Q1. Sort Age in Ascending Order
import pandas as pd
Age = [25,18,30,22]
df=pd.DataFrame({'Age':Age})
print(df.sort_values(by='Age'))



## Q2. Sort Marks in Descending Order
Marks = [70, 95, 80, 60]
df=pd.DataFrame({'Marks':Marks})
print(df.sort_values(by='Marks',ascending=False))



## Q3. Find Mean Age
Age = [20, 25, 30, 25]
df=pd.DataFrame({'Age':Age})
print(df.mean())


## Q4. Find Median Marks
Marks = [50, 60, 70, 80, 90]
df=pd.DataFrame({'Marks':Marks})
print(df.median())


## Q5. Find Mode
Age = [20, 25, 25, 30, 25]
df=pd.DataFrame({'Age':Age})
print(df.mode())


## Q6. Find Maximum Score
Score = [78, 90, 67, 88]
df=pd.DataFrame({'Score':Score})
print(df.max())

## Q7. Find Minimum Score
print(df.min())


## Q8. Count City Frequency
City = ['Bhopal','Indore','Bhopal','Jabalpur']
df=pd.DataFrame({'City':City})
print(df.value_counts())


## Q9. Find Percentage Frequency
City = ['A','A','B','C']
df=pd.DataFrame({'City':City})
print(df.value_counts(normalize=True)*100)


## Q10. Sort DataFrame by Salary
df=pd.DataFrame({"Name" : [ "Aman","Raj","Riya"],
'Salary':[30000,50000,40000]})
print(df.sort_values(by='Salary'))


## Q11. Find Correlation
Math = [10,20,30,40]
Science = [15,25,35,45]
df=pd.DataFrame({'Math':Math,'Science':Science})
print(df.corr())


# q12  find covariance
Math = [10,20,30,40]
Science = [15,25,35,45]
df=pd.DataFrame({'Math':Math,'Science':Science})
print(df.cov())



## Q13. Sort by Two Columns
Age = [20, 25, 30, 25]
City = ['Bhopal','Indore','Bhopal','Jabalpur']
df=pd.DataFrame({'Age':Age,
                 'City' : City})
print(df.sort_values(by='City'))
print(df.sort_values(by='Age'))



## Q14. Student Statistics
Marks = [60,70,80,90]
df=pd.DataFrame({'Marks':Marks})
print(df.min())
print(df.max())
print(df.mean())
print(df.median())



## Q15. Mini Practice
# Create a DataFrame with:
# Name, Age, Score, Height
# Tasks:
# 1. Sort by Score (Descending)
# 2. Find Mean Age
# 3. Find Median Height
# 4. Show Score Frequency
df=pd.DataFrame({
    'Name':['ajitesh','ajay'],
    'Age':[20,25],
    "Height":[181,178],
    'Score':[89,75]
        })
print(df.sort_values(by="Score",ascending=False))
print(df['Age'].mean())
print(df['Height'].median())
print(df['Score'].value_counts())