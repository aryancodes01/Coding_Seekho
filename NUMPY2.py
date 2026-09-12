"""
import numpy as np
crr= np.array([[1,2,3],[4,5,6]])
drr= np.array([[1,7,3],[4,9,6]])
print(crr*drr)# index wise multiplication kr rha h 
OUTPUT:
[[ 1 14  9]
 [16 45 36]]
  
print(crr @ drr) #for matrix actual multiplication 
print(crr.dot(drr))#  for matrix actual multiplication 

import numpy as np

crr = np.array([[1, 2],
                [4, 5]])

drr = np.array([[7, 8],
                [9, 10],
                [11, 12]])

print(np.linalg.det(crr))# for determinant 


import numpy as np

crr = np.array([[1, 2],
                [4, 5]])

drr = np.array([[7, 8],
                [9, 10],
                [11, 12]])

print(np.linalg.det(crr))
print(np.linalg.inv(crr))

OUTPUT:
-2.9999999999999996
[[-1.66666667  0.66666667]
 [ 1.33333333 -0.33333333]]
 
 
 fancy indexing = ek saath multiple array element access kr skte hai for example : print(arr[[0,1,2,3]]) and print(arr[[arr>=90]])
"""
import numpy as np

crr = np.array([[1, 2],
                [4, 5]])

drr = np.array([[7, 8],
                [9, 10],
                [11, 12]])

print(np.linalg.det(crr))
print(np.linalg.inv(crr))