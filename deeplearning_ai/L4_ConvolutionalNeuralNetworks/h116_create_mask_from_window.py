import numpy as np
from deeplearning_ai.L4_ConvolutionalNeuralNetworks.h110_utils import *


def create_mask_from_window(x):
    """
    Creates a mask from an input matrix x, to identify the max entry of x.

    Arguments:
    x -- Array of shape (f, f)

    Returns:
    mask -- Array of the same shape as window, contains a True at the position corresponding to the max entry of x.
    """

    ### START CODE HERE ### (≈1 line)
    mask = x == np.max(x)
    ### END CODE HERE ###

    return mask


def create_mask_from_window_test():
    np.random.seed(1)
    x = np.random.randn(2,3)
    mask = create_mask_from_window(x)
    print('x = ', x)
    print("mask = ", mask)


if __name__ == "__main__":
    create_mask_from_window_test()