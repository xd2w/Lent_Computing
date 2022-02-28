from .station import MonitoringStation
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    record = []
    for station in stations:
        if station.typical_range_consistent() and station.latest_level_consistent():
            if station.relative_water_level() > tol:
                record.append((station.name, station.relative_water_level()))
    return sorted_by_key(record, 1, reverse=True)

def stations_highest_rel_level(stations, N):
    record = []
    record_top_N = []
    for station in stations:
        if station.typical_range_consistent() and station.latest_level_consistent():
            record.append((station.name, station.relative_water_level()))
        record_sorted = sorted_by_key(record, 1, reverse=True)
    for i in range(N):
        record_top_N.append(record_sorted[i])
    return record_top_N