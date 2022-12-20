from matplotlib import animation
from matplotlib import pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")


def animation_2D(x: np.array, y: np.array, z: list, interval: float = 0.1):
    def update_plot_2D(frame):
        nonlocal plot
        plot.remove()
        plot = ax.pcolormesh(x, y, z[frame], cmap='magma')
        return plot,
    fig = plt.figure(figsize=(100, 100), dpi=200)
    ax = plt.axes()
    plot = ax.pcolormesh(x, y, z[0])
    plt.xlabel('X')
    plt.ylabel('Y')
    fig.colorbar(plot, ax=ax)
    ax.set_title('2D Heat map')
    animate = animation.FuncAnimation(fig, update_plot_2D, len(z), interval=interval)
    plt.show()


def animation_3D(x: np.array, y: np.array, z: list, interval: float = 0.1):
    def update_plot_3D(frame):
        nonlocal plot
        plot.remove()
        plot = ax.plot_surface(x, y, z[frame], cmap='magma')
        return plot,
    fig = plt.figure(figsize=(100, 100), dpi=200)
    ax = plt.axes(projection='3d')
    plot = ax.plot_surface(x, y, z[0])
    fig.colorbar(plot, ax=ax)
    ax.set_title('3D Heat map')
    animate = animation.FuncAnimation(fig, update_plot_3D, len(z), interval=interval)
    plt.show()