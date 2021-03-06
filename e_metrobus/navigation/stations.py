import os
from typing import Dict

import pandas
from django.conf import settings

from e_metrobus.navigation.constants import DataPerKilometer, VEHICLES, FLEET_CONSUMPTION

STATIONS_FILE = os.path.join(settings.APPS_DIR, "navigation", "stations.csv")


class Stations:
    def __init__(self, filename):
        self.stations = pandas.read_csv(filename, index_col=0)
        self.__init_stations()

    def __init_stations(self):
        # Mirror diagonal:
        for i, station in enumerate(self.stations):
            self.stations[station] = self.stations.iloc[i]

        # Distances in meter -> kilometer:
        self.stations = self.stations / 1000

    @staticmethod
    def __calc_route_data(km, vehicle):
        return vehicle.data * km

    def get_stations(self):
        return [station for station in self.stations]

    def get_distance(self, from_station: str, to_station: str) -> float:
        return self.stations[from_station][to_station]

    def get_route_data(
        self, from_station: str, to_station: str
    ) -> Dict[str, DataPerKilometer]:
        distance = self.get_distance(from_station, to_station)
        return {
            vehicle.name: self.__calc_route_data(distance, vehicle)
            for vehicle in VEHICLES
        }

    def get_fleet_data(self):
        distance = FLEET_CONSUMPTION.distance
        return {
            vehicle.name: self.__calc_route_data(distance, vehicle)
            for vehicle in VEHICLES
        }

    def get_route_data_for_vehicle(
        self, from_station: str, to_station: str, vehicle: str
    ) -> DataPerKilometer:
        distance = self.get_distance(from_station, to_station)
        i = 0
        while i < len(VEHICLES):
            if VEHICLES[i].name == vehicle:
                return VEHICLES[i].data * distance
            i += 1
        raise KeyError("Vehicle not found", vehicle)

    def __getitem__(self, item):
        return self.stations.index[item]


STATIONS = Stations(STATIONS_FILE)
DEFAULT_STATIONS = [0, len(STATIONS.stations) - 1]
