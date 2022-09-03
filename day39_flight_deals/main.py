#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import logging as l
from pprint import pformat, pprint

l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', 
              level=l.INFO, datefmt='%I:%M:%S')

from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()


f_deals = dm.get_flight_deals()
# l.info(f"\n{pformat(f_deals, width=200)}")

for deal in f_deals:
    # l.info(deal['city'])
    deal['iataCode'] = fs.get_iata_code(deal['city'])
    body = {
        "price": {
            "city": deal['city'],
            "iataCode" : deal['iataCode'],
            "lowestPrice" : deal['lowestPrice']
        }
    }
    dm.update_iata_code(body, deal['id'])

l.info(f"\n--1--\n{pformat(f_deals, width=200)}")

fd = FlightData(f_deals, 'LON')
fd.get_flight_data()

l.info(f"\n--2--\n{pformat(f_deals, width=200)}")

