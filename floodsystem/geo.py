# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from .station import MonitoringStation
from haversine import haversine, Unit #import haversine

#implement function to return list of station and distance
def stations_by_distance(stations, p):
        list_of_distance = []
        for station in stations:
            list_of_distance.append((station.name, haversine(p, station.coord)))
        return(sorted_by_key(list_of_distance, 1))

def stations_within_radius(stations, centre, r):
    list_of_stations = []
    for station in stations:
        distance = haversine(centre, station.coord)
        if distance <= r:
            list_of_stations.append(station)
    return(list_of_stations)

def rivers_with_station(stations):
    """returns the list rivers where the stations are located"""

    river_list = set([])
    for each_station in stations :
        river_list.add(each_station.river)

    return list(river_list)


def stations_by_river(stations):
    """returns a dictionary where key is the name of river 
    and the the item is a list of stations on that river"""

    river_dict = dict([])

    for station in stations :
        keys = river_dict.keys()

        if station.river in keys:
            river_dict[station.river].append(station)

        else:
            river_dict[station.river] = [station]

    return river_dict

def rivers_by_station_number(stations, N):
    """returns top N number of rivers with greatest number of stations """

    river_dict = stations_by_river(stations)
    for key in river_dict.keys():
        river_dict[key] = [station.name for station in river_dict[key]]

    list_of_rivers = []

    for key in river_dict.keys():
        list_of_rivers.append( (key, len(river_dict[key])) )

    list_of_rivers = sorted_by_key(list_of_rivers, 1, reverse=True)

    end_list = list_of_rivers[:N]

    while list_of_rivers[N-1][1] == list_of_rivers[N][1]:
        end_list.append(list_of_rivers[N])
        N += 1

    return end_list
