"""_summary_
Searches with Kiwi API the flights database for cheap flights. Also provides IATA code.
Returns:
    _type_: str:IATA code & list: cheap flight data.
"""
import os
from datetime import datetime, timedelta
import requests

KIWI_API_KEY = os.environ.get("KIWI_API_KEY")

KIWI_LOCATIONS_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
KIWI_HEADER={
    "apiKey":KIWI_API_KEY
}

class FlightData:
    """_summary_
    Searches with Kiwi API the flights database for cheap flights. Also provides IATA code.
    Returns:
        _type_: str:IATA code & list: cheap flight data.
    """
    def __init__(self):
        pass

    def iata_code(self, location_name:str, location_type:str):
        """
        Searches KIWI db for the IATA code of a country/city/airtport.

        Args:
            location_name (str): input from spreadsheet country/city/airtport name
            location_type (str): describe is name is country/city/airtport

        Returns:
            str: IATA_code
        """
        iata_code = ""
        parameters={
            "term":location_name,
            "location_types":location_type
        }

        response = requests.get(KIWI_LOCATIONS_ENDPOINT, params=parameters, headers=KIWI_HEADER)
        data = response.json()
        try:
            iata_code = data['locations'][0]['code']
        except IndexError:
            pass
        return iata_code

    def search (self, fly_to, price_to):
        """
        Searchs flights in KIWI database
        Args:
            fly_to (str): IATA code of the destination
            price_to (str): max price to pay for tickets

        Returns:
            dict: flight_data in the format provided by KIWI and for the first (cheapest)
                  result of the search.
        """
        #today + 15 days as starting day from
        days_to_start = 20
        days_to_end_start = 150
        current_date = datetime.now() #datetime.strftime(datetime.now(), '%d/%m/%Y')
        initial_start_date = current_date + timedelta(days=days_to_start)
        final_start_date = initial_start_date + timedelta(days=days_to_end_start)

        initial_start_date = datetime.strftime(initial_start_date, '%d/%m/%Y')
        final_start_date = datetime.strftime(final_start_date, '%d/%m/%Y')


        parameters = {
            "adults":2,
            "adult_hand_bag":"1,0",
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 5,
            "fly_from": "NL",
            "max_stopovers":1,
            "fly_to": fly_to,
            "date_from": initial_start_date,
            "date_to": final_start_date,
            "curr":"EUR",
            "price_to": price_to,
            "fly_days": "4,5,6",
            "fly_days_type": "departure"
        }

        response = requests.get(KIWI_SEARCH_ENDPOINT, params=parameters, headers=KIWI_HEADER)
        data = response.json()

        try:
            return data['data'][0]

        except:
            return ""
