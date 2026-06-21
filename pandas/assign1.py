# ques 1  
import pandas as pd
print(pd.__version__)


# ques 2 
arr=pd.Series([1,2,3,4,5])
print(arr)


# ques 3 
arr=pd.Series(['aman','rahul','neha','priya'])
print(arr)


# ques 4 
arr=pd.Series({
    "maths":80,
    "science":75,
    "english":90
})
print(arr)


# ques 5
name=['ajitesh']
age=[20]
print(pd.DataFrame([name,age]))


# ques 6 
employee=['john']
sal=[10000]
print(pd.DataFrame([employee,sal]))


# ques 7 
matrix=[[1,2],
        [3,4],
        [5,6]]
print(pd.DataFrame(matrix))



# ques  8 
pro=['laptop','phone']
price=[20000,5000]
print(pd.DataFrame([pro,price]))


# ques 9 
name=['ajay','akshat','ajitesh']
marks=[60,70,80]
arr=pd.DataFrame({'name':name,
                  'marks':marks})
print(arr.info())

# ques 10 
print(arr)



