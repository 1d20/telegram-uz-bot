import json
import requests


class BookingClient:
    _base_url = 'https://booking.uz.gov.ua/{}/purchase/'.format('en')

    def __init__(self):
        pass

    def get_stations(self, name):
        response = requests.get(self._base_url + 'station/?term={}'.format(name))
        return json.loads(response.content)
