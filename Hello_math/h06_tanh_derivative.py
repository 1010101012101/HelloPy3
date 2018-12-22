import numpy as np
import matplotlib.pyplot as plt


def tanh_derivative(x):
    return 1-np.tanh(x)**2


x = np.arange(-2,2,0.1)

y1 = np.tanh(x)
y2 = tanh_derivative(x)

print("sigmoid(0):", np.tanh(0))
print("sigmoid_derivative(0):", tanh_derivative(0))

#plt.plot(x,y1)
plt.plot(x,y2)
#plt.plot(x,x)

plt.show()
