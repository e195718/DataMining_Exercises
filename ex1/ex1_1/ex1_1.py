import math
import numpy as np
import matplotlib.pyplot as plt

def true_function(x):
    '''
    >>> true_function(0)
    0.0
    '''
    y = np.sin(np.pi * x * 0.8) * 10
    return y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111)

    ax.set_xlabel("x", fontsize = 10)
    ax.set_ylabel("y", fontsize = 10)

    x = np.arange(-1.0, 1.1, 0.1)
    ax.plot(x, true_function(x), label = "y = sin(π*x*0.8)*10")

    ax.legend(loc = "lower right")

    plt.show()