from uz_api import mock_data
from itertools import chain
from uz_api.models import Station, Train, Coach
from uz_api.serializers import Serializer
from uz_api.booking import BookingClient


class ClientInteface:
    def __init__(self, language='en'):
        self.client = BookingClient()

    def stations(self, name):
        stations = [Station.from_dict(station) for station in self.client.get_stations(name)]
        return stations

    def trains(self, station_from_id, station_to_id, date_dep, time_dep="00:00", time_dep_till=None,
               another_ec=0, search=''):
        """
        date_dep format: mm.dd.yyyy
        """
        trains = [Train.from_dict(train) for train in mock_data.TRAINS['value']]
        return trains

    def coaches(self, station_from_id, station_to_id, date_dep, train, model, coach_type, round_trip=0, another_ec=0):
        """
        date_dep: 1463224100
        coach_type: С2
        model: 3
        train: 043
        """
        coaches = [Coach.from_dict(train) for train in mock_data.COACHES['coaches']]
        return coaches

    def seats(self, station_from_id, station_to_id, date_dep, train, coach_num,
              coach_class, coach_type_id, change_scheme):
        return set(chain(*mock_data.COACH['value']['places'].values()))


if __name__ == '__main__':
    client = ClientInteface()

    print(client.stations('Ky'))
    print(client.stations('Lv'))
    # print(Serializer.serialize(client.stations('Ky')))
    #
    # print(client.trains(100, 42, '01.01.2000'))
    # print(Serializer.serialize(client.trains(100, 42, '01.01.2000')))
    #
    # print(client.coaches(100, 42, 1463224100, '043', 3, 'C2'))
    # print(Serializer.serialize(client.coaches(100, 42, 1463224100, '043', 3, 'C2')))
    #
    # print(client.seats(100, 42, 1463224100, '043', 1, 2, 19, 1))
