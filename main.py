from spreadsheet_manager import SpreadsheetManager
from flight_search_api import FlightSearchAPI
from notification_manager import NotificationManager
from flight_data_manager import find_cheapest_flight
import time
from datetime import datetime, timedelta
from pprint import pprint

# ======================= SET UP ============================
data_manager = SpreadsheetManager()
spreadsheet_data = data_manager.get_destination_data()
flight_search = FlightSearchAPI()
notification_manager = NotificationManager()
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

# Obtain user emails
user_data = data_manager.get_user_emails()
user_email_list = [row["email"] for row in user_data]
# print(f"Email list: {user_email_list}")

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

    # Account for if there are no direct flights for the destination; check for cheapest indirect flights
    if cheapest_flight.price == "N/A":
        print(
            f"No direct flights to {destination['city']}. Trying for indirect flights..."
        )
        stopover_flights = flight_search.check_flights(
            "LON",
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False,
        )
        cheapest_flight = find_cheapest_flight(stopover_flights)
        print(f"Cheapest indirect flight price: £{cheapest_flight.price}")

    # ================ SENDING NOTIFICATIONS/EMAILS ====================
    if (
        cheapest_flight.price != "N/A"
        and cheapest_flight.price < destination["lowestPrice"]
    ):
        # Customise the message depending on the number of stops
        if cheapest_flight.stops == 0:
            message = (
                f"Low price alert! Only £{cheapest_flight.price} to fly direct "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
            )
        else:
            message = (
                f"Low price alert! Only £{cheapest_flight.price} to fly "
                f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                f"with {cheapest_flight.stops} stop(s) "
                f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."
            )

        print(f"Check your email. Lower price flight found to {destination['city']}!")

        # SMS
        # notification_manager.send_sms(message_body=message)

        # Whatsapp
        # notification_manager.send_whatsapp(message_body=message)

        # Send email to all users
        notification_manager.send_emails(email_list=user_email_list, email_body=message)
