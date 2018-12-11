import numpy as np


import numpy as np
a = [1,2,3,4,5,6]
result = np.lib.pad(a, pad_width=(2,3), mode='constant', constant_values=0)
print(result)

b = [[1, 2],
     [3, 4]]

result = np.lib.pad(b, pad_width=(2,2), mode='constant', constant_values=0)
print(result)
np.max()
np.argmax()