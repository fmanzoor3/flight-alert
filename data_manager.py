import requests
from requests.auth import HTTPBasicAuth
import os
from dotenv import load_dotenv
from pprint import pprint

# Load env variables
load_dotenv()


class DataManager:

    def __init__(self):

        self._user = os.environ["SHEETY_USERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.prices_endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self._authenticaion_token = os.environ["SHEET_AUTHENTICATION_TOKEN"]
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=self.prices_endpoint,
            headers={"Authorization": f"Bearer {self._authenticaion_token}"},
        )
        data = response.json()
        # pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{self.prices_endpoint}/{city['id']}",
                json=new_data,
                headers={"Authorization": f"Bearer {self._authenticaion_token}"},
            )
            # print(response.text)
