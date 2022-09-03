import requests
import logging as l
l.basicConfig(format='[%(asctime)s.%(msecs)03d] %(message)s', 
              level=l.INFO, datefmt='%I:%M:%S')

SHEETY_URL_GET = "https://api.sheety.co/fd81df72098a976484ecf693894c0fc3/flightDeals/prices"
SHEETY_URL_PUT = "https://api.sheety.co/fd81df72098a976484ecf693894c0fc3/flightDeals/prices/"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    
    def __init__(self):
        pass
    
    def get_flight_deals(self) -> list:
        # response = requests.get(
        #     url=SHEETY_URL_GET, 
        #     headers = {
        #         "Authorization": "Basic YmNjaG86aW1nb29k",
        #         }
        #     )
        # l.info(f"{self.response.json()}")
        # rsp_list = response.json()['prices']
        rsp_list = [
            {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54},
            {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42},
            {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485},
            {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551},
            {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95},
            {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414},
            {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240},
            {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260},
            {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378}]
        
        return rsp_list
        
    def update_iata_code(self, body, id) -> None:
        pass
        # response = requests.put(
        #     url=f"{SHEETY_URL_PUT}{id}", 
        #     json=body,
        #     headers = {
        #         "Authorization": "Basic YmNjaG86aW1nb29k",
        #         }
        #     )
        
        # print(f"{URL_PUT}{id}") 
        # print(body)               
        # l.info(response)
        

        