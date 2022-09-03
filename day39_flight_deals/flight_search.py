import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def __init__(self):
        pass
    
    def get_iata_code(self, city: str) -> str:
        response = requests.get(
            url="https://tequila-api.kiwi.com/locations/query", 
            params={
                "term": city,
                "location_types": "city"
                },
            headers={
                "apikey": "NeM50Vgbpp7cHGL-V8Bcna1SkAa3CeNB",
                })
        
        # print(response.json()['locations'][0]['code'])
        return response.json()['locations'][0]['code']


    def get_lowest_flight(
                self,
                deal,
                fly_from, 
                date_from, 
                date_to,
                nights_in_dst_from, 
                nights_in_dst_to) -> None:
        
        response = requests.get(
            url="https://tequila-api.kiwi.com/v2/search", 
            params={
                "fly_from": fly_from,
                "fly_to" : deal['iataCode'],
                "date_from" : date_from,
                "date_to" : date_to,
                "nights_in_dst_from" : nights_in_dst_from,
                "nights_in_dst_to" : nights_in_dst_to,
                "one_for_city" : 1,
                "flight_type": "round",
                "max_stopovers": 0,                
                "curr" : "GBP",                
                },
            headers={
                "apikey": "NeM50Vgbpp7cHGL-V8Bcna1SkAa3CeNB",
                })
        
        # print(response.json()['locations'][0]['code'])
        # print(response.json())
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {deal['iataCode']}.")
            return None
        
        deal['price'] = data["price"],
        # origin_city=data["route"][0]["cityFrom"],
        deal['origin_airport']=data["route"][0]["flyFrom"],
        # destination_city=data["route"][0]["cityTo"],
        deal['destination_airport']=data["route"][0]["flyTo"],
        deal['out_date']=data["route"][0]["local_departure"].split("T")[0],
        deal['return_date']=data["route"][1]["local_departure"].split("T")[0]
            
        return