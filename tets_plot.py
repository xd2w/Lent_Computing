#!/usr/bin/env python3

import numpy as np
from floodsystem.plot import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels, fetch_station_data

def tets_plot_water_levels():
    try:
        stations = build_station_list()
        station = stations[912]
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        plot_water_levels(station, dates, levels, test=True)

        assert True

    except:
        assert False

if __name__ == "__main__":
    tets_plot_water_levels()