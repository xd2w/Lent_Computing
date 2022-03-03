from floodsystem.flood import *
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.pyplot as plt
import numpy as np

def run():
    stations = build_station_list()
    update_water_levels(stations)

    risk_dict  = dict()

    for station in stations:
        risk = station.risk_level()
        if risk is None:
            continue
        if risk in risk_dict.keys():
            risk_dict[risk] += 1

        else:
            risk_dict[risk] = 1

    print("low", risk_dict["low"])
    print("moderate", risk_dict["moderate"])
    print("high", risk_dict["high"])
    print("extream", risk_dict["extream"])
    

if __name__ == "__main__":
    run()