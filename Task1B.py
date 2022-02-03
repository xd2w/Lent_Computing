from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()
list_of_distance = stations_by_distance(stations,(52.2053, 0.1218))
print(list_of_distance[:10])
print("\n")
print(list_of_distance[-10:])