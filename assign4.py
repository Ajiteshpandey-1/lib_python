# ques 1 : fancy indexing  
import numpy as np
arr1=np.array([10,20,30,40,50,60])
index=[0,2,4]
print(arr1[index])


# ques 2 : fancy indexing 
import numpy as np
arr1=np.array([10,20,30,40,50,60])
index=[0,-1]
print(arr1[index])


# ques3 : fancy indexing  
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[[0,1,2],[0,1,2]])


# ques 4  :conitional selection and print val greater than 15 
import numpy as np 
arr=np.array([5,12,18,25,30,7])
print(arr[arr>15])


# ques 5 : even values  
import numpy as np 
arr=np.array([5,12,18,25,30,7])
print(arr[arr%2==0])


# ques 6 : sorting  
import numpy as np 
arr=np.array([25,10,40,5,30])
print(np.sort(arr))


# ques 7  :find sorted indices 
import numpy as np 
arr=np.array([50,20,70,10])
print(arr.argsort())



# ques 8 : concated array 
import numpy as np 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.array([arr1,arr2])
print(arr.flatten())


# ques  9 :vertical stacking 
import numpy as np 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.vstack((arr1,arr2)))


# ques 10  : horizontal stacking 
import numpy as np 
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.hstack((arr1,arr2)))