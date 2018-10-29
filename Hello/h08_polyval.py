import numpy as np
import matplotlib.pyplot as plt

x_data = np.random.rand(30).astype(np.float32)
y_data = x_data * 0.1 + 0.3

poly = np.polyfit(x_data, y_data, deg=1)

plt.plot(x_data, y_data, 'o')
plt.plot(x_data, np.polyval(poly, x_data))
plt.show()
