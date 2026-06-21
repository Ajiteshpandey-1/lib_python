import pandas as pd
import numpy as np 
# ques 1 
matrix=np.random.randint(1,10,(3,3))
print(matrix)

# or 
matrix=np.array([[1,2,3],
        [4,5,6],
        [7,8,9]])
print(matrix)


# ques 2 
matrix=np.array([[1,2,3],
        [4,5,6],
        [7,8,9]])
print(matrix*2)


# ques 3 for row wise sum we use axis =1 
matrix=np.array([[1,2,3],
        [4,5,6],
        [7,8,9]])
print(matrix.sum(axis=1))


# ques 4 
matrix=np.array([[1,2,3],
        [4,5,6],
        [7,8,9]])
print(matrix.sum(axis=0))


# ques 5 
matrix=np.array([[1,2,3],
        [4,5,6],
        [7,8,9]])
print(matrix[1])


# ques 6 
df=pd.DataFrame({
    'name':['raj','amit','neha','priya'],
    'marks':[80,70,90,85]
})
print(df)

# ques 7
df=pd.DataFrame({
    'name':['raj','amit','neha','priya'],
    'marks':[80,70,90,85]
})
df['bonus']=df['marks']+5
print(df)


# ques 8 
df=pd.DataFrame({
    'name':['raj','amit','neha','priya'],
    'marks':[80,70,90,85]
})
print(df[df['marks']>80])



# ques 9 
df=pd.DataFrame({
    'name':['raj','amit','neha','priya'],
    'marks':[80,70,90,85]
})
print(df.iloc[0])

# ques 10
df=pd.DataFrame({
    'name':['raj','amit','neha','priya'],
    'marks':[80,70,90,85]
})
print(df.iloc[2])