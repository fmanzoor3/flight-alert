from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
import time
from datetime import datetime, timedelta
from pprint import pprint

# ======================= SET UP ============================
data_manager = DataManager()
spreadsheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
# pprint(spreadsheet_data)

# Update/Generate IATA codes in our spreadsheet
for row in spreadsheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slow down requests to avoid rate limit
        time.sleep(2)
# pprint(f"spreadsheet_data:\n {spreadsheet_data}")

data_manager.destination_data = spreadsheet_data
data_manager.update_destination_codes()

# =================== FLIGHT SEARCH ============================
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in spreadsheet_data:
    print(f"Searching direct flights for {destination['city']}...")
    flights = flight_search.check_flights(
        "LON",
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: £{cheapest_flight.price}")
    # Slowing down requests to avoid rate limit
    time.sleep(2)
