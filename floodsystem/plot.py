#!/usr/bin/env python3

import matplotlib.pyplot as plt
import datetime
import numpy as np


def plot_water_levels(station, dates, levels, *args, test=False ):
    # plots a graph of date against leveles

    low , high = station.typical_range

    low = np.ones_like(dates) * low
    high = np.ones_like(dates) * high

    # plots the fetched date
    fig, ax = plt.subplots(1,1,figsize=(12, 5))
    ax.plot(dates, levels, label="water level")
    ax.plot(dates, low, "--", label="typical low")
    ax.plot(dates, high, "--", label="typical high")
    ax.legend()
    plt.suptitle(station.name)

    if not test:
        plt.show()

