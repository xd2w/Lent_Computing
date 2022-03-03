from floodsystem.flood import stations_highest_rel_level, stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def test_stations_highest_rel_level():
    station_list = build_station_list()
    update_water_levels(station_list)
    highest_list = stations_highest_rel_level(station_list, 10)
    assert(highest_list[1][1] != None)

def test_stations_level_over_threshold():
    station_list = build_station_list()
    update_water_levels(station_list)
    list_over_threshold = stations_level_over_threshold(station_list, 0.1)
    assert(list_over_threshold[1] != None)
