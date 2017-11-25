import numpy as np


class Machine:
    '''
    Tree parity machine.  Generates a binary digit for a given random vector
    '''

    def __init__(self, k=3, n=4, r=6):
        self.k = k
        self.n = n
        self.r = r
        self.W = np.random.randint(-1, r + 1, [k, n])
