import numpy as np

def list_to_nparray(l):
    return np.reshape(l, [1, len(l)])
