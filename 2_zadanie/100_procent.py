
from __future__ import division  # Division in Python 2.7
import os
from matplotlib import colors
import colorsys as cs
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib


def gradient_rgb_gbr(v):
    if v <= 0.5:
        return (0, 1 - 2 * v, 2 * v)
    else:
        v = v - 0.5
        return (2 * v, 0, 1 - 2 * v)


def gradient_rgb_gbr_full(v):
    if v < 0.25:
        return (0, 1, 4 * v)
    elif v < 0.5:
        v = v - 0.25
        return (0, 1 - 4 * v, 1)
    elif v < 0.75:
        v = v - 0.5
        return (4 * v, 0, 1)
    else:
        v = v - 0.75
        return (1, 0, 1 - 4 * v)


def create_custom_colormap():
    # Define a custom colormap with a black and white gradient
    custom_colors = [gradient_rgb_gbr_full(i) for i in np.linspace(0, 1, 256)]
    custom_cmap = LinearSegmentedColormap.from_list(
        "custom_bw", custom_colors, N=256)
    return custom_cmap


def plot_examples(colormaps, elevation_data):
    """
    Helper function to plot data with associated colormap.
    """

    n = len(colormaps)
    fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                            layout='constrained', squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(elevation_data, cmap=cmap,
                            rasterized=True, vmin=40, vmax=155)
        fig.colorbar(psm, ax=ax)
        ax.invert_yaxis()  # Reverse the Y-axis
    plt.show()


def main():
    print(1)

    dem_file = r'C:\Users\barte\Desktop\Komunikacja\2_zadanie\big.dem'
    elevation_data = []
    h = 0
    w = 0
    cm = 0
    # Open the DEM file and read its contents line by line
    with open(dem_file, 'r') as file:
        for i, line in enumerate(file):
            if i == 0:
                # Split the first line into separate values
                w, h, cm = line.split()
            else:
                # Split the other lines into individual values and convert to numbers (assuming they are numbers)
                data_values = [float(value) for value in line.split()]
                elevation_data.append(data_values)

        print("Width:", w)
        print("Height:", h)
        print("cm:", cm)

        print(min(min(row) for row in elevation_data))
    cmap = create_custom_colormap()
    plot_examples([cmap], elevation_data)


if __name__ == "__main__":
    main()
