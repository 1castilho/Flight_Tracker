# Flight_Tracker
Track flights to help plan vacation or small trips

## Objective
Create a tool to track flights listed in an online spreadsheet, compare with a maximum cost and send an sms if lower prices are found, including: cost, origin, destination and dates.
The spreadsheet should contain the following headers: 
1. Destination: with destination city, airport or country name.
1. Type: identifying whether 'Destination' contains a city, airport or country.
1. IATA_Code: this field can remain blank and is populated by the script.
1. Max_Price: this field should stay blank until 'IATA_Code' is populated. Later, populate it if the max price for the flight price search.

In addition to the python scripts, the folder must have a 'number.py' file which contains your phone number and a twilio account phone number.

Also, a 'credentials.json' with Google Spreadsheet credentials is necessary for the code to work. Finally, API keys mentioned in the code must also be created in Twilio, Kiwi and Google.

Resources:
1. [Kiwi Partners Flight Search API](https://partners.kiwi.com/)
1. [Tequila Flight Search API Documentation](https://tequila.kiwi.com/portal/docs/tequila_api)