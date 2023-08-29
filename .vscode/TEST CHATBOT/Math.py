import numpy as np
A = np.array([[2,4,3,6],[3,4,5,6],[1,2,3,4],[5,6,7,8]])
print(A)
Ainv = np.linalg.inv(A)
print(Ainv)
C = np.array([9,8,7,6]).T
print(C)
print(Ainv.dot(C))