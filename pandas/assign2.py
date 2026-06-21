# ques 1 
import pandas as pd
name=['aman','rahul','neha','priya','ravi']
age=[21,22,20,23,24]
arr=pd.DataFrame({
    'name':name,
    'age':age
})
print(arr.head(3))


# ques 2 
name=['aman','rahul','neha','priya','ravi']
age=[21,22,20,23,24]
arr=pd.DataFrame({
    'name':name,
    'age':age
})
print(arr.tail(2))


# ques 3 
name=['aman','rahul','neha','priya','ravi']
age=[21,22,20,23,24]
arr=pd.DataFrame({
    'name':name,
    'age':age
})
print((arr.info()))



# ques 4 
data={
    'name':['ajay','ajitesh'],
    'age':[20,22],
    'gender':['m','m']}
df=pd.DataFrame(data)
print(df.shape)
print(df.dtypes)



# ques 5 
data={
    'name':['ajay','ajitesh'],
    'age':[20,22],
    'gender':['m','m']}
df=pd.DataFrame(data)
print(df.loc[0:2,['name','age','gender']])


# ques 6 
data={
    'name':['ajay','ajitesh','raj','mudit'],
    'age':[20,22,22,23],
    'gender':['m','m','m','m']}
df=pd.DataFrame(data)
print(df.iloc[1,0:2])


# ques 7 
data={
    'name':['ajay','ajitesh','raj','mudit'],
    'age':[20,22,22,23],}
df=pd.DataFrame(data)
print(df.rename(columns={'age':'marks'}))



# ques 8 
data={
    'name':['ajay','ajitesh','raj','mudit'],
    'age':[20,22,22,None],}
df=pd.DataFrame(data)
print(df.fillna(24))



# ques 9
city=["bpl",'ind','bpl']
df=pd.DataFrame(city)
df=df.replace({'bpl':'bhopal',
               'ind':"indore"})
print(df)


# ques 10 
city=["bpl",'ind','bpl']
df=pd.DataFrame(city)
# duplicated 
new=df.duplicated()
print(new)
# drop_duplicates() 
new=df.drop_duplicates()
print(new)
