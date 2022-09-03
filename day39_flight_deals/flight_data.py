from datetime import datetime, timedelta
import logging as l
from flight_search import FlightSearch

class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, deals:list, departure_code):
        self.deals = deals
        self.departure_code = departure_code
        
    def get_flight_data(self) -> list:
        today = datetime.now()
        date_from = (today + timedelta(days=1)).strftime("%d/%m/%Y")
        date_to = (today + timedelta(days=180)).strftime("%d/%m/%Y")
        
        l.info(f"date_from: {date_from}")
        l.info(f"date_to: {date_to}")
        
        fs = FlightSearch()
        
        for deal in self.deals:
            # l.info(f"date_to: {date_to}")
            
            fs.get_lowest_flight(
                deal,
                self.departure_code, 
                date_from, 
                date_to,
                7, 
                28)
        
        return self.deals