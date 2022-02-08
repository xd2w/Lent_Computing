#!/usr/bin/env python3
"""Unit test for the station module"""

from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation
from floodsystem.geo import *

stations = build_station_list()

def test_stations_by_distance():
    s_id = "test-s-0"
    m_id = "test-m-0"
    label = "T0"
    coord = (2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "Test"
    town = "Test"
    s0 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-1"
    m_id = "test-m-1"
    label = "T1"
    coord = (10.0, 20.0)
    trange = (-2.3, 3.4445)
    river = "Test"
    town = "Test"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-2"
    m_id = "test-m-2"
    label = "T2"
    coord = (50.0, 100.0)
    trange = (-2.3, 3.4445)
    river = "Test"
    town = "Test"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    station_list = [s0, s1, s2]

    assert stations_by_distance(station_list, (0, 0)) == [('T0', 497.19868760742435), ('T1', 2476.1748308545807), ('T2', 10720.167161626012)]


def test_stations_within_radius():
    s_id = "test-s-0"
    m_id = "test-m-0"
    label = "T0"
    coord = (2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "Test"
    town = "Test"
    s0 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-1"
    m_id = "test-m-1"
    label = "T1"
    coord = (10.0, 20.0)
    trange = (-2.3, 3.4445)
    river = "Test"
    town = "Test"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id = "test-s-2"
    m_id = "test-m-2"
    label = "T2"
    coord = (50.0, 100.0)
    trange = (-2.3, 3.4445)
    river = "Test"
    town = "Test"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    station_list = [s0, s1, s2]
    
    list_in_radius = stations_within_radius(station_list, (0, 0), 500)
    first = list_in_radius[0]
    assert first.name == "T0"


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



