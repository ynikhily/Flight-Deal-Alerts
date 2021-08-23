# THIS PIECE OF CODE IS RESPONSIBLE FOR READING AND WRITING TO AN ONLINE GOOGLE SHEET USING SHEETY API
# READ THE SHEETY DOCUMENTATION FOR MORE INFORMATION ON HOW TO USE IT.
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/d1593f92fbc5fe6e0a71c28bfa4d7b4c/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/d1593f92fbc5fe6e0a71c28bfa4d7b4c/flightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def add_user(self, firstname, lastname, email):
        user_param = {
            'user': {
                'firstName': firstname,
                'lastName': lastname,
                'email': email
            }
        }
        add_response = requests.post(url=SHEETY_USERS_ENDPOINT, json=user_param)
        add_response.raise_for_status()
        print(add_response.text)

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)