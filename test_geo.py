#!/usr/bin/env python3
"""Unit test for the station module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

stations = build_station_list()

def test_rivers_with_station():
    """test rivers_with_stationn"""
    rivers = rivers_with_station(stations)

    assert len(rivers) > 0
    assert type(rivers) in [list, tuple]

def test_stations_by_river():
    """tests stations_by_river"""
    river_dict = stations_by_river(stations)

    assert len(river_dict) > 0
    assert type(river_dict) is dict

def test_rivers_by_station_number():
    """test rivers_by_station_number"""
    top10_rivers = rivers_by_station_number(stations, 10)

    assert len(top10_rivers) >= 10

    if len(top10_rivers) > 10:
        for i in range(len(top10_rivers) - 10):
            if top10_rivers[9+i] != top10_rivers[10+i]:
                assert False

        assert True



