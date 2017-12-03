# UZ API Client

## Install

```bash
pip install git+git://github.com/1d20/uz-api
```

## Usage

```python
>>> from uz_api import ClientInteface, Serializer
>>> client = ClientInteface()
>>> client.stations('Ky')
[Station('2200001', 'Kyiv'), Station('2201180', 'Kyivska Rusanivka'), Station('2031278', 'Kyj'), Station('2011189', 'Kykshor')]
>>> Serializer.serialize(client.stations('Ky'))
[{'station_id': '2200001', 'title': 'Kyiv'}, {'station_id': '2201180', 'title': 'Kyivska Rusanivka'}, {'station_id': '2031278', 'title': 'Kyj'}, {'station_id': '2011189', 'title': 'Kykshor'}]
>>> client.trains(100, 42, '01.01.2000')
[Train(1, 1, '743Л', '5:01', [CoachType('С1', 117, 'Seating first class'), CoachType('С2', 176, 'Seating second class')], Station(2200001, 'Darnytsya'), Station(2218000, 'Lviv'), UZTimestamp(1465741200, '2016-06-12 17:20:00'), UZTimestamp(1465759260, '2016-06-12 22:21:00')), Train(0, 0, '091К', '7:25', [CoachType('Л', 11, 'Suite / first-class sleeper'), CoachType('К', 50, 'Coupe / coach with compartments')], Station(2200001, 'Kyiv-Pasazhyrsky'), Station(2218000, 'Lviv'), UZTimestamp(1465760460, '2016-06-12 22:41:00'), UZTimestamp(1465787160, '2016-06-13 06:06:00'))]
>>> Serializer.serialize(client.trains(100, 42, '01.01.2000'))
[{'category': 1, 'model': 1, 'num': '743Л', 'travel_time': '5:01', 'types': [{'letter': 'С1', 'places': 117, 'title': 'Seating first class'}, {'letter': 'С2', 'places': 176, 'title': 'Seating second class'}], 'till': {'station': 'Lviv', 'station_id': 2218000, 'date': 1465759260, 'src_date': '2016-06-12 22:21:00'}, 'from': {'station': 'Darnytsya', 'station_id': 2200001, 'date': 1465741200, 'src_date': '2016-06-12 17:20:00'}}, {'category': 0, 'model': 0, 'num': '091К', 'travel_time': '7:25', 'types': [{'letter': 'Л', 'places': 11, 'title': 'Suite / first-class sleeper'}, {'letter': 'К', 'places': 50, 'title': 'Coupe / coach with compartments'}], 'till': {'station': 'Lviv', 'station_id': 2218000, 'date': 1465787160, 'src_date': '2016-06-13 06:06:00'}, 'from': {'station': 'Kyiv-Pasazhyrsky', 'station_id': 2200001, 'date': 1465760460, 'src_date': '2016-06-12 22:41:00'}}]
>>> client.coaches(100, 42, 1463224100, '043', 3, 'C2')
[Coach(False, '2', 10, False, 1, 21, {'А': 35831}, 1700, []), Coach(False, '2', 9, False, 3, 21, {'А': 35831}, 1700, [])]
>>> Serializer.serialize(client.coaches(100, 42, 1463224100, '043', 3, 'C2'))
[{'allow_bonus': False, 'coach_class': '2', 'coach_type_id': 10, 'has_bedding': False, 'num': 1, 'places_cnt': 21, 'prices': {'А': 35831}, 'reserve_price': 1700, 'services': []}, {'allow_bonus': False, 'coach_class': '2', 'coach_type_id': 9, 'has_bedding': False, 'num': 3, 'places_cnt': 21, 'prices': {'А': 35831}, 'reserve_price': 1700, 'services': []}]
>>> client.seats(100, 42, 1463224100, '043', 1, 2, 19, 1)
{'47', '36', '55', '38', '48', '12', '56', '49', '27', '37', '16', '42', '18', '32', '34', '8', '43', '28', '22', '39', '33'}
```

## Links

https://github.com/master94/UaTrainTicketsBookingClient
https://habrahabr.ru/post/303150/
