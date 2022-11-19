# Flight_Tracker
Track flights to help plan vacation or small trips

## Objective
Create a tool to track flights listed in an online spreadsheet, compare with a maximum cost and print a message if lower prices are found, including: cost, origin, destination and dates.

*Note:* Twilio module is not active, but the module `notification.py` allows sending SMS via Twilio.

## Setup Before Use
### Create KIWI API Account
Use links below and create a Kiwi account. No need for a paid account.

Resources:
1. [Kiwi Partners Flight Search API](https://partners.kiwi.com/)
1. [Tequila Flight Search API Documentation](https://tequila.kiwi.com/portal/docs/tequila_api)

### Google Spreadsheet
Create a google spreadsheet:
1. Using google sheets to read, write and append data. Not an easy task and demanded a lot of searching the web to be able to interface with google sheets. Finally found a good video on Youtube [in this link](https://www.youtube.com/watch?v=4ssigWmExak).

The google spreadsheet must have a tab named 'Flight_Wishlist' which must contain the following headers:
1. Destination: with destination city, airport or country name.
1. Type: identifying whether 'Destination' contains a city, airport or country.
1. IATA_Code: this field can remain blank and is populated by the script.
1. Max_Price: populate it if the max price for the flight price search. If no lower price is found, returns blank.

Once this step is complete you should also have a `credentials.json` saved to your folder, carrying your own data.

### Changes to python scripts:
On `main.py`, update the following:
1. Update the value of `SPREADSHEET_ID` to your own google spreadsheet.
On `flight_data.py`, update the following:
1. Update `KIWI_API_KEY` to your own Kiwi api key. **Be careful not to share your key on the web!**
