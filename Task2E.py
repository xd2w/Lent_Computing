#!/usr/bin/env python3

from floodsystem.plot import *
import datetime

stations = build_station_list()
station = stations[1]

plot_water_levels(station, datetime.datetime(2022, 2, 3, 0,0), 0)