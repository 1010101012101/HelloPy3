import numpy as np

from dnn_utils_v2 import sigmoid, sigmoid_backward, relu, relu_backward

# GRADED FUNCTION: L_model_forward

def L_model_forward(X, parameters):
    """
    Implement forward propagation for the [LINEAR->RELU]*(L-1)->LINEAR->SIGMOID computation

    Arguments:
    X -- data, numpy array of shape (input size, number of examples)
    parameters -- output of initialize_parameters_deep()

    Returns:
    AL -- last post-activation value
    caches -- list of caches containing:
                every cache of linear_activation_forward() (there are L-1 of them, indexed from 0 to L-1)
    """

    caches = []
    A = X
    L = len(parameters) // 2  # number of layers in the neural network

    # Implement [LINEAR -> RELU]*(L-1). Add "cache" to the "caches" list.
    for l in range(1, L):
        A_prev = A
        ### START CODE HERE ### (≈ 2 lines of code)
        A, cache = relu(np.dot(parameters['W' + str(l)], A_prev) + parameters['b' + str(l)])
        caches.append((cache, A))
        ### END CODE HERE ###

    # Implement LINEAR -> SIGMOID. Add "cache" to the "caches" list.
    ### START CODE HERE ### (≈ 2 lines of code)
    AL, cache = sigmoid(np.dot(parameters['W' + str(L)], A) + parameters['b' + str(L)])
    caches.append((cache, AL))
    ### END CODE HERE ###

    assert (AL.shape == (1, X.shape[1]))

    return AL, caches
