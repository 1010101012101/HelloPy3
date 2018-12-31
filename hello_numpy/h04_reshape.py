import numpy as np


arr=np.arange(16).reshape(2,2,4)
print(arr)
print("HHHA:0====>")
# print(arr.transpose(0,2,1))
# print("HHHA:1====>")
# print(arr.swapaxes(1,2))
# print("HHHA:2====>")
print(arr.swapaxes(0,1))
print("HHHA:3====>")
print(arr.swapaxes(1,0))