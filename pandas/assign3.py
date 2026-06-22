# ques 1
import pandas as pd
df=pd.DataFrame({
    'name':['aman','riya',None],
    'age':[21,pd.NaT,25]
})
print(df.isna())


# ques 2
df=pd.DataFrame({
    'name':['aman',None,'raj'],
    'age':[20,None,25]
})
print(df.isnull().sum())


# ques 3
df=pd.DataFrame({
    'name':['aman','raj'],
    'age':[20,None]
})
df['age']=df['age'].fillna(df['age'].mean())
print(df)


# ques 4
df=pd.DataFrame({
    'city':['bpl',None],
    'age':[20,None]
})
print(df['city'].fillna('unknown'))


# ques 5
df=pd.DataFrame({
    'name':['aman','raj'],
    'age':[20,None]
})
print(df.dropna())


# ques 6
df=pd.DataFrame({
    'age':[20,85,68]
})
print(df['age'].astype(float))


# ques 7
df=pd.DataFrame({
    'city':['bpl','ind','delhi']
})
print(df['city'].replace('delhi','new delhi'))


# ques 8 
df=pd.DataFrame({
    'score':[89,85,68]
})
print(df['score'].replace(89,67))


# ques 9 
df=pd.DataFrame({
    'age':[20,85,68],
    'name':['aman','raj','rajjo']
})
print(df.drop('age',axis=1))

# ques 10 
df=pd.DataFrame({
    'age':[20,85,68],
    'name':['aman','raj','rajjo']
})
print(df.drop(index=1,axis=0))