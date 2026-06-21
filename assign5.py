# quest 1 
import numpy as np 
arr1=np.array([1,2,3,4,5])
print(arr1.shape)
print(arr1.ndim)
print(arr1.size)
print(arr1.dtype)


# ques 2
import numpy as np  
arr=np.random.randint(1,20,(3,3))
print(arr)

# ques 3
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr[1])
print(arr[2])
print(arr[-1])


# ques 4 
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[2:6:])


# ques 5 
arr=np.array([1,2,3,4,5,6,7,8])
index=[2,4]
print(arr[index])


# ques 6 
arr=np.array([1,21,13,42,35,6,27,8])
print(arr[arr>15])


# ques 7 
arr=np.array([1,2,3,4,5,6,7,8])
print(arr+5)


# ques 8 
arr=np.array([1,2,3,4,5,6,7,8])
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())



# ques 9 
arr=np.array([1,2,3,4,5,6,7,8])
newarr=np.sort(arr)
print(newarr)


# ques 10 
arr1=np.array([1,2,3,4,5,6,7,8])
arr2=np.array([1,2,3,4,5,6,7,8])
arr=np.array([arr1,arr2])
print(arr.flatten())


#ques 10
import numpy as np 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.vstack((arr1,arr2)))