import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-3, 3, 0.1)
y = np.exp(x)

plt.plot(x, y)
plt.show()
