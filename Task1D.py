#!/usr/bin/env python3
"""This pyhton file demostrates the use of floodsystem.geo.rivers_with_station() 
and floodsystem.geo.stations_by_river()"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def main():
    """main functon that demonstrates the functions"""

    stations = build_station_list()
    rivers  = rivers_with_station(stations)

    first_10 = rivers[:10]
    first_10.sort()
    print(str(len(rivers))+" stations")
    print("fist 10 stations : ")
    print(first_10)
    print()

    river_dict = stations_by_river(stations)

    list1 = river_dict["River Aire"]
    list1 = [station.name for station in list1]

    list2 = river_dict["River Cam"]
    list2 = [station.name for station in list2]

    list3 = river_dict["River Thames"]
    list3 = [station.name for station in list3]

    list1.sort()
    list2.sort()
    list3.sort()

    print("Stations on River Aire: \n")
    print(list1)
    print("\nStations on River Cam: \n")
    print(list2)
    print("\nStations on River Thames: \n")
    print(list3)


if __name__ == "__main__":
    main()