import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    fig = plt.figure()
    fig.suptitle('No axes on this figure')
    fig, ax_lst = plt.subplots(2, 2)
