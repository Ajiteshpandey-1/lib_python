# ques 1 :  add both arrays element wise 
import numpy as np 
arr1=np.array([1,2,3,4])
arr2=np.array([10,20,30,40])
print(arr1+arr2)



# ques 2 : multiply aray element - wise 
import numpy as np 
arr1=np.array([1,2,3,4])
arr2=np.array([10,20,30,40])
print(arr1 * arr2)



# ques 3 : add a scalar to an array
import numpy as np 
arr1=np.array([10,20,30,40])
print(arr1+5)



# ques 4 : multiply arry by a scalar 
import numpy as np 
arr1=np.array([10,20,30,40])
print(arr1*5)



# ques 5 : create 2d array and add 10 to every element 
import numpy as np 
arr1=np.array([[10,20,30,40],[50,60,70,80]])
print(arr1+10)



# ques 6 : find sum of array 
import numpy as np 
arr1=np.array([10,20,30,40])
print(arr1.sum())



# ques 7 : find mean of array 
import numpy as np 
arr1=np.array([10,20,30,40])
print(arr1.mean())



# ques 8 : find maximum and minimum value 
import numpy as np 
arr1=np.array([10,20,30,40])
print(f" maximum : {arr1.max()}")
print(f"minimum : {arr1.min()}")



# ques 9 : row wise sum using axis 
import numpy as np 
arr1=np.array([[10,20,30,40],[50,60,70,80]])
print(np.sum(arr1,axis=1))



# ques 10 : column wise sum using axis 
import numpy as np 
arr1=np.array([[10,20,30,40],[50,60,70,80]])
print(np.sum(arr1,axis=0))