#!/usr/bin/env python3

from calendar import timegm
import matplotlib.pyplot as plt
import datetime
import numpy as np

from .datafetcher import fetch_measure_levels
from .stationdata import build_station_list

def plot_water_levels(station, date, levels):
    # plots a graph for the date (datetime.datetime object) given 

    now = datetime.datetime.today()
    dates = date.replace(tzinfo=None) 

    # working the difference in time between today and the date
    dt = now - date + datetime.timedelta(minutes=1)

    # fetching the data from dt ago
    dates, levels = fetch_measure_levels(station.measure_id, dt=dt)

    print(dates[-1], now-dt)

    # checks if the data is avilables for that date, if not ends the precedure
    if (dates[-1].replace(tzinfo=None) - date.replace(tzinfo=None)) > datetime.timedelta(days=1):
        print("Error data for the date not found")
        return None


    time = dates[-97:]
    water_level = levels[-97:]

    low , high = station.typical_range
    low = np.ones_like(time) * low
    high = np.ones_like(time) * high

    # plots the fetched date
    plt.plot(time, water_level)
    # plt.plot(time, low, "--")
    # plt.plot(time, high, "--")
    plt.show()

