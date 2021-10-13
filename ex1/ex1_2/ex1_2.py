import sys
sys.path.append("../ex1_1")
import pandas as pd
from ex1_1 import true_function
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def plot_point():
    random.seed(0)
    cols = ['観測点', '真値']
    global df 
    df= pd.DataFrame(index=[], columns=cols)

    for i in range(20):
        x = random.uniform(-1,1)
        y = true_function(x)
        record = pd.Series([x,y], index=df.columns)
        df = df.append(record, ignore_index=True)
    return df


if __name__ == '__main__':
    plot_point()
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111)

    ax.set_xlabel("x", fontsize = 10)
    ax.set_ylabel("y", fontsize = 10)

    x = np.arange(-1.0, 1.1, 0.1)
    ax.plot(x, true_function(x), label = "y = sin(π*x*0.8)*10")
    plt.scatter(df['観測点'], df['真値'], c='k', s=10)

    ax.legend(loc = "lower right")

    plt.show()