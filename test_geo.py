#!/usr/bin/env python3
"""Unit test for the station module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

stations = build_station_list()

def test_rivers_with_station():
    rivers = rivers_with_station(stations)

    assert len(rivers) > 0
    assert type(rivers) in [list, tuple]

def test_stations_by_river():
    river_dict = stations_by_river(stations)

    assert len(river_dict) > 0
    assert type(river_dict) is dict
