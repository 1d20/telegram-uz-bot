STATIONS = {
  "value": [
    {
      "title": "Kyiv",
      "station_id": "2200001"
    },
    {
      "title": "Kyivska Rusanivka",
      "station_id": "2201180"
    },
    {
      "title": "Kyj",
      "station_id": "2031278"
    },
    {
      "title": "Kykshor",
      "station_id": "2011189"
    }
  ],
  "error": None,
  "data": {
    "req_text": [
      "ky",
      "лн"
    ]
  },
  "captcha": None
}

TRAINS = {
  "value": [
    {
      "num": "743Л",
      "model": 1,
      "category": 1,
      "travel_time": "5:01",
      "from": {
        "station_id": 2200001,
        "station": "Darnytsya",
        "date": 1465741200,
        "src_date": "2016-06-12 17:20:00"
      },
      "till": {
        "station_id": 2218000,
        "station": "Lviv",
        "date": 1465759260,
        "src_date": "2016-06-12 22:21:00"
      },
      "types": [
        {
          "title": "Seating first class",
          "letter": "С1",
          "places": 117
        },
        {
          "title": "Seating second class",
          "letter": "С2",
          "places": 176
        }
      ],
      "reserve_error": "reserve_24h"
    },
    {
      "num": "091К",
      "model": 0,
      "category": 0,
      "travel_time": "7:25",
      "from": {
        "station_id": 2200001,
        "station": "Kyiv-Pasazhyrsky",
        "date": 1465760460,
        "src_date": "2016-06-12 22:41:00"
      },
      "till": {
        "station_id": 2218000,
        "station": "Lviv",
        "date": 1465787160,
        "src_date": "2016-06-13 06:06:00"
      },
      "types": [
        {
          "title": "Suite / first-class sleeper",
          "letter": "Л",
          "places": 11
        },
        {
          "title": "Coupe / coach with compartments",
          "letter": "К",
          "places": 50
        }
      ],
      "reserve_error": "reserve_24h"
    }
  ],
  "error": None,
  "data": None,
  "captcha": None
}


COACHES = {
  "coach_type_id": 10,
  "coaches": [
    {
      "num": 1,
      "type": "С",
      "allow_bonus": False,
      "places_cnt": 21,
      "has_bedding": False,
      "reserve_price": 1700,
      "services": [],
      "prices": {
        "А": 35831
      },
      "coach_type_id": 10,
      "coach_class": "2"
    },
    {
      "num": 3,
      "type": "С",
      "allow_bonus": False,
      "places_cnt": 21,
      "has_bedding": False,
      "reserve_price": 1700,
      "services": [],
      "prices": {
        "А": 35831
      },
      "coach_type_id": 9,
      "coach_class": "2"
    }
  ],
  "places_allowed": 8,
  "places_max": 8
}


COACH = {
  "value": {
    "places": {
      "А": [
        "8",
        "12",
        "16",
        "18",
        "22",
        "27",
        "28",
        "32",
        "33",
        "34",
        "36",
        "37",
        "38",
        "39",
        "42",
        "43",
        "47",
        "48",
        "49",
        "55",
        "56"
      ]
    }
  },
  "error": None,
  "data": None,
  "captcha": None
}
