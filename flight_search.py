
import requests
from flight_data import FlightData

# CREATE A FREE ACCOUNT ON TEQUILA TO USE THEIR API AT https://tequila.kiwi.com/portal/login
# READ THEIR API DOCUMENTATION TO GET MORE FAMILIAR WITH IT.
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = ""

# THIS CLASS WORKS TO FETCH THE DATA USING TEQUILA API AND GET FLIGHT DETAILS AS REQUESTED.
class FlightSearch:

    def __init__(self):
        self.header = {"apikey": TEQUILA_API_KEY}

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=self.header, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def search_flights(self, origin, destination, today, future_date ):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        search_query = {
            'fly_from': origin,
            'fly_to': destination,
            'date_from': today,
            'date_to': future_date,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        try:
            search_response = requests.get(url=search_endpoint, params=search_query, headers=self.header)
            search_response.raise_for_status()
            search_result = search_response.json()['data'][0]

        except IndexError:
            print(f"No flights found for {destination}")
            return None

        flight_data = FlightData(search_result['price'], search_result['cityFrom'], search_result['flyFrom'],
                                 search_result['cityTo'], search_result['flyTo'],
                                 search_result['route'][0]['local_departure'].split('T')[0],
                                 search_result['route'][1]['local_departure'].split('T')[0])

        print(f"{flight_data.origin_city} ---> {flight_data.destination_city}: £{flight_data.price}")
        return flight_data
