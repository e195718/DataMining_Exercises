import sys
from pandas.core.frame import DataFrame
sys.path.append("../ex1_1")
sys.path.append("../ex1_2")
from ex1_2 import plot_point
from ex1_1 import true_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

def make_dataset(dataset: pd.DataFrame, average=0.0, std=2.0) -> pd.DataFrame:
    size = len(dataset)
    noisy = np.random.normal(loc=average, scale=std, size=size)
    noisy_data = dataset["真値"] + noisy
    dataset["観測値"] = noisy_data
    return dataset

if __name__ == '__main__':
    df = plot_point()
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111)

    ax.set_xlabel("x", fontsize = 10)
    ax.set_ylabel("y", fontsize = 10)

    x = np.arange(-1.0, 1.1, 0.1)
    ax.plot(x, true_function(x), label = "y = sin(π*x*0.8)*10")
    make_dataset(df)
    plt.scatter(df['観測点'], df['真値'], c='k', s=10)
    plt.scatter(df['観測点'], df['観測値'], c='r', s=10)

    ax.legend(loc = "lower right")

    plt.show()
    