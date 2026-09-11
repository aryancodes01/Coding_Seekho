"""
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)

import sys
total = sys.getsizeof(arr)+ sum([sys.getsizeof(x) for x in arr])
print(total)
a=arr.nbytes # for calculating size of an array in numpy
print(a)


import numpy as np

arr=np.array([1,2,3,4,5,5,6,6,6,7,7,7,8,8,99,9,9,0])
brr=np.arange(100)
crr=np.array([[1,2,3],[4,5,6]])
drr=([[[3,4],2,3,[5,6],[7,8]]])
print(arr.nbytes)# size of the total elements 
print(crr.shape)# shows the shape just like how many 
print(crr.dtype)# shows the data type 
print(crr.size)#no. of elements kitne hai 
print(crr.ndim)# shows the dimensions of the array 

OUTPUT :
144
(2, 3)
int64
6
2


import numpy as np

err = np.ones((3,4),dtype=np.int64)
print(err.dtype)
print(err)
OUTPUT:
int64
[[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]
 
 import numpy as np

err = np.eye((3),dtype=np.int64)
print(err.dtype)
print(err)
OUTPUT:
int64
[[1 0 0]
 [0 1 0]
 [0 0 1]]
 
 # SLICING
 import numpy as np
arr=np.array([1,2,3,4,5,5,6,6,6,7,7,7,8,8,99,9,9,0])
print(arr[2:6:2])

OUTPUT:
[3 5]
"""
import numpy as np
arr=np.array([1,2,3,4,5,5,6,6,6,7,7,7,8,8,99,9,9,0])
hrr = arr[1:5].copy()# now only hrr will change phle agar copy nhi lga tha to arr bhi change ho rha tha 
hrr[0]=23
print(hrr)
print(arr[1:2])
a= np.sum(hrr)
print(a)
print(np.min(hrr))