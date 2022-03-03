#!/usr/bin/env python3

import datetime
from turtle import update
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels



def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    high_risk_name = stations_highest_rel_level(stations, 6)
    high_risk_name = [name for name, level in high_risk_name]
    high_risk_stations = []
    
    for station in stations:

        if station.name == "Letcombe Bassett":
            continue

        if station.name in high_risk_name:
            high_risk_stations.append(station)


    for station in high_risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=100))
        plot_water_levels(station, dates, levels)

if __name__ == "__main__":
    run()
