import numpy as np
import matplotlib.pyplot as plt


def show_depth(depths, figsize=(8, 4),
               title="Sonar sweep",
               ylabel="depth", xlabel="distance from the submarine"):
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(-depths, lw=1, c='k')
    ax.fill_between(range(len(depths)), -depths,
                     -np.max(depths),
                     fc='darkolivegreen', hatch='///')
    ax.fill_between(range(len(depths)), -depths, 0,
                     color='dodgerblue', alpha=.6)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    fig.suptitle(title);