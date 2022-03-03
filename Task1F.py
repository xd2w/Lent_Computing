#!/usr/bin/env python3
"""This file demonstrates the use of method """

from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    inconsistent  = inconsistent_typical_range_stations(stations)
    inconsistent = [station.name for station in inconsistent]
    inconsistent.sort()
    print(inconsistent)

if __name__ == "__main__":
    run()