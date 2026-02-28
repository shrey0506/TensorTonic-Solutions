import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    sigmoid_res = 1/(1+np.exp(-np.array(x)))
    return sigmoid_res