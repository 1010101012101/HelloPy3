import numpy as np


x = np.array([[1,2,3]])
print(x)
print(np.swapaxes(x, 0, 1))

x = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
print(x)


print(np.swapaxes(x, 0, 2))

