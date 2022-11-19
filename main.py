from datetime import datetime
from google_spreadsheet import GoogleSpreadsheets
from flight_data import FlightData
from notification import Notification

# TODO: switch from SMS to mail

SPREADSHEET_ID = "1Pn0BXe6OyFZNaASoDrxmw4AemzA9SSZCFRf-cMULIes"
WEEKDAY = {
    0:"Mon",
    1:"Tue",
    2:"Wed",
    3:"Thu",
    4:"Fri",
    5:"Sat",
    6:"Sun"
}

notification = Notification()
sheets = GoogleSpreadsheets(SPREADSHEET_ID)
flight = FlightData()

def get_iata_code():
    """
    IATA codes are the country/city/airport codes with 2/3 letters used to id every
    one of these in the world. Function reads data on spreadsheet and writes missing IATA
    codes.
    Returns:
    This function returns list of IATA codes based on name and type (country/city/airport).
        _type_: list
    """
    destination_list = sheets.read('Flight_Wishlist')

    for destination in destination_list:

        if len(destination) == 2:
            location_name = destination[0]
            location_type = destination[1].lower()

            destination.append(flight.iata_code(location_name, location_type))

    sheets.write('Flight_Wishlist', destination_list)

    return destination_list


def get_flight_price(destination_list:list):
    """_summary_
    With the list of destination (country/city/airport) and max price, searches
    for a predefined 6months range and for specific weekdays (hard coded) to find
    and return via SMS/mail the ones that are below max price for 2 travellers.
    """
    for destination in destination_list:
        max_price = destination[-1]
        dest = destination[-2]

        flight_dict = flight.search(dest, max_price)
        if len(flight_dict) > 1:
            try:
                departure_date = flight_dict['route'][0]['local_departure'].split('T')[0]
                return_date = flight_dict['route'][1]['local_departure'].split('T')[0]
                departure_weekday = WEEKDAY[datetime.strptime(departure_date, "%Y-%m-%d").weekday()]
                return_weekday = WEEKDAY[datetime.strptime(return_date, "%Y-%m-%d").weekday()]

                message = f"Only €{flight_dict['price']} to fly from {flight_dict['cityFrom']}-{flight_dict['flyFrom']} to {flight_dict['cityTo']}-{flight_dict['flyTo']} from {departure_date}({departure_weekday}) to {return_date}({return_weekday})."
                #notification.send_sms(message)
                print(message)
            except TypeError:
                pass

get_flight_price(get_iata_code())
