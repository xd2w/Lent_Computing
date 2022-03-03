#!/usr/bin/env python3

import numpy as np
from matplotlib.dates import date2num
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    # returns the polinomial of pth pawwer that best describes the data
    t = date2num(dates)
    d0 = t[0]
    poly_coeff = np.polyfit(t-d0,levels, p)
    square_fit_poly = np.poly1d(poly_coeff)

    return (square_fit_poly, d0)

def plot_water_level_with_fit(station, dates, levels, p, *args, test=False):
    # plots the least-square bit polynomical wit degree of p for the data
    poly, d0 = polyfit(dates, levels, p)
    t = date2num(dates)

    low , high = station.typical_range
    low = np.ones_like(dates) * low
    high = np.ones_like(dates) * high

    fig, ax = plt.subplots(1,1,figsize=(12, 5))

    ax.plot(dates, levels, label="water levels")
    ax.plot(dates, poly(t-d0), label="polyfit")
    ax.plot(dates, low, "--", label="typical low")
    ax.plot(dates, high, "--", label="typical high")
    plt.title(station.name)
    ax.legend()

    if not test:
        plt.show()


    