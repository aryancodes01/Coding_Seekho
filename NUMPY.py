"""
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)

import sys
total = sys.getsizeof(arr)+ sum([sys.getsizeof(x) for x in arr])
print(total)
a=arr.nbytes # for calculating size of an array in numpy
print(a)








"""
import numpy as np

arr=np.array([1,2,3,4,5,5,6,6,6,7,7,7,8,8,99,9,9,0])
brr=np.arange(100)
crr=([[1,2,3],[4,5,6]])
drr=([[[3,4],2,3,[5,6],[7,8]]])
print(brr)
print(arr)
print(crr)
print(drr)