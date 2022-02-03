# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit #import haversine

#implement function to return list of station and distance
def stations_by_distance(stations, p):
        list_of_distance = []
        for station in stations:
            list_of_distance.append((station.name, haversine(p, station.coord)))
        return(sorted_by_key(list_of_distance, 1))