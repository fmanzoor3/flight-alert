from data_manager import DataManager
from flight_search import FlightSearch
import time
from pprint import pprint

data_manager = DataManager()
spreadsheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
# pprint(spreadsheet_data)

for row in spreadsheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slow down requests to avoid rate limit
        time.sleep(2)
# pprint(f"spreadsheet_data:\n {spreadsheet_data}")

data_manager.destination_data = spreadsheet_data
data_manager.update_destination_codes()
