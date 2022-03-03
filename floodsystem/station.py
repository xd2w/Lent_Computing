# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """"returns False if the low/high value is inconsistent or None, and True otherwise"""
        if self.typical_range is None:
            return False

        low, high = self.typical_range

        if low > high:
            return False

        return True

    def latest_level_consistent(self):
        if self.latest_level == None:
            return False
        else:
            return True

    def relative_water_level(self):
        if self.typical_range_consistent() and self.latest_level_consistent():
            low, high = self.typical_range
            rel_level = (self.latest_level - low) / (high - low)
        else:
            rel_level = None
        return rel_level

    def risk_level(self):
        rel_level = self.relative_water_level()

        if rel_level is None:
            return None

        if rel_level < 0.8:
            return "low"

        elif rel_level < 1.5:
            return "moderate"

        elif rel_level < 2:
            return "high"

        else:
            return "extream"


def inconsistent_typical_range_stations(stations):
    """"returns the station with inconsistent typical low/high values"""
    inconsistent  = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent.append(station)

    return inconsistent
    

