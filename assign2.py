# ques 1  : use methods of numpy
import numpy as np
arr=np.array([10,20,30,40])
print(arr.shape)   #shape deta hai (4,1)
print(arr.ndim)  # dimension batata hai 1 ya 2 ya 3
print(arr.size)  # size batata hai elements kitne hai 
print(arr.dtype)  # data type 


# ques 2 : find shape of array 
import numpy as np
arr=np.array([5,25,10,20,30,4])
print(arr.shape)


# ques 3 : 1d indexing
import numpy as np
arr=np.array([5,25,10,20,30,4])
print(arr[0])  # first element 
print(arr[-1])   #last element



# ques  4 : print 5 using 2D indexing
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[1:2,1:2])



# ques 5 : print 9 by 2d indexing  
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[2,2])


# ques 6:  print from index 1 to 4 using slicing 
import numpy as np
arr=np.array([5,25,10,20,30,4])
print(arr[1:5])


# ques 7 print the first 5 elements 
import numpy as np
arr=np.array([5,25,10,20,30,4])
print(arr[:5])


# ques 8 2D slicing first 2 rows 
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0:2,0:])


# ques 9  
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0:,0:2])



# que 10 : boolean indexing 
import numpy as np 
arr=np.array([2,4,10,24,13,7])
print(arr>5)