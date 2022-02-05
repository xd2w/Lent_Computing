from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

stations = build_station_list()
list_within_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)
list_of_names = []
for station in list_within_radius:
    list_of_names.append(station.name)
print(sorted(list_of_names))
