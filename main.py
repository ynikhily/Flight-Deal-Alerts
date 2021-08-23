# IMPORT ALL NECESSARY CLASSES AND MODULES
import datetime as dt
from data_manager import DataManager
from flight_search import FlightSearch
from twilio.rest import Client

# CREATE A FREE TWILIO ACCOUNT AND GET YOUR VALUES FOR BELOW MENTIONED VARIABLES
account_sid = ""
auth_token = ""

ORIGIN_CITY = "LON"  # ORIGIN AIRPORT'S IATA CODE

# OBJECT INITIALISATION FOR DATA MANAGER AND FLIGHT SEARCH
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print(sheet_data)

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    # print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
now = dt.datetime.now()
new_date = now.date() + dt.timedelta(weeks=24)
today_date = now.date().strftime("%d/%m/%Y")
date_after = new_date.strftime("%d/%m/%Y")

for destination in sheet_data:

    flight = flight_search.search_flights(
        ORIGIN_CITY,
        destination["iataCode"],
        today_date,
        date_after
    )

    if flight == None:
        pass

    elif flight.price <= destination["lowestPrice"]:
        print(f"sending message for {flight.destination_city}")

        message_body = f"Flight to {flight.destination_city} from {flight.origin_city} on {flight.out_date}" \
                       f"just for {flight.price} pounds"

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=message_body,
            from_='',  # ENTER YOUR TWILIO ACCOUNT NUMBER HERE
            to=''  # ENTER YOUR PERSONAL NUMBER ON WHICH YOU WISH TO RECEIVE ALERTS ALONG WITH YOUR COUNTRY CODE
        )
        print(message.status)
# Or send mail to users gained through user acquisition
