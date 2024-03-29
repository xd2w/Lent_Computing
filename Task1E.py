#!/usr/bin/env python3
"""This file demonstrates the use of function rivers_by_station_number()
from floodsystem.geo"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    stations = build_station_list()
    river_list = rivers_by_station_number(stations, 9)

    print(river_list)


if __name__ == "__main__":
    run()