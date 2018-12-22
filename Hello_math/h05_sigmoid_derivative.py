import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1/(1+np.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x)*(1-sigmoid(x))


x = np.arange(-5,5,0.1)

y1 = sigmoid(x)
y2 = sigmoid_derivative(x)

print("sigmoid(0):", sigmoid(0))
print("sigmoid_derivative(0):", sigmoid_derivative(0))

#plt.plot(x,y1)
plt.plot(x,y2)
#plt.plot(x,0.25*x+0.5)

plt.show()

