# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    """tests floodsystem.station.typical_range_consistent()"""
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    station = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert station.typical_range_consistent() is True

    station.typical_range = None

    assert station.typical_range_consistent() is False    

    station.typical_range = (5.09, -1.23)

    assert station.typical_range_consistent() is False   

def test_inconsistent_typical_range_stations():
    """tests inconsistent_typical_range_stations() from floodsystem.station submodule"""
    station1 = MonitoringStation("1", "1", "station1", (0, 0), (1, 2), "River", "Town")
    station2 = MonitoringStation("2", "1", "station2", (0, 0), None, "River", "Town")
    station3 = MonitoringStation("2", "1", "station3", (0, 0), (1, -2), "River", "Town")

    stations = [station1, station2, station3]

    inconsistent = inconsistent_typical_range_stations(stations)

    assert len(inconsistent) == 2

    for station in inconsistent:
        assert  station.station_id == "2"


