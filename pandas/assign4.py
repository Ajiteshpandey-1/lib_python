# ques 1
import pandas as pd
df=pd.DataFrame({
    'name':['ajitesh','heer','ajay','rashi'],
    'age':[20,22,21,22]
})
print(df['name'])


# ques 2
df=pd.DataFrame({
    'name':['ajitesh','heer','ajay','rashi'],
    'marks':[20,22,21,19]
})
print(df[['name','marks']])


# ques 3
df=pd.DataFrame({
    'name':['ajitesh','heer','ajay','rashi'],
    'marks':[20,22,21,19]
})
print(df[df['marks']>20])


# ques 4
df=pd.DataFrame({
    'name':['ajitesh','aman','ajay'],
    'city':['bpl','anganbaadi','indore']
})
print(df[df['city']=='bpl'])


# ques 5
df=pd.DataFrame({
    'marks':[45,50,70,80,65]
})
print(df['marks'].max())


# ques 6
df=pd.DataFrame({
    'age':[20,22,21,22]
})
print(df['age'].min())


# ques 7 
df=pd.DataFrame({
    'marks':[45,50,70,80,65]
})
print(df['marks'].sort_values())


# ques 8
df=pd.DataFrame({
    'city':['bpl','anganbaadi','indore']
})
print(df['city'].value_counts())


# ques 9 
df=pd.DataFrame({
    'marks':[45,50,70],
    'city':['bpl','anganbaadi','indore']
})
print(df.groupby('city')['marks'].mean())


# ques 10 
df=pd.DataFrame({
    'age':[20,22,21,22,35],
    'marks':[45,50,70,80,65]
})
print(df[(df['marks']>70 ) & (df['age'] > 21)])