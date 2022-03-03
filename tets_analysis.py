
import numpy as np
import datetime
from floodsystem.analysis import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels, fetch_station_data

def test_polyfit():
    stations = build_station_list()
    station = stations[912]
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
    poly, d0 = polyfit(dates, levels, 4)


    if type(d0) is not np.float64:
        assert False

    if type(poly) is not np.poly1d:
        assert False

    assert True
    

def test_plot_water_level_with_fit():
    try:
        stations = build_station_list()
        station = stations[912]
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=2))
        plot_water_level_with_fit(station, dates, levels, 4, test=True)

        assert True

    except:
        assert False


if __name__ == "__main__":
    test_polyfit()
    test_plot_water_level_with_fit()