# FlightAlert

## Project Overview
FlightAlert is here to help you find and be notified about affordable flights. Sign up to receive alerts when flight prices to popular destinations drop below a certain price. This project integrates various APIs to make everything work seamlessly.

## Features
-**Popular Destinations and Price Limits**: We track popular destinations and their affordable-price threshold using a Google Spreadsheet.
-**Flight Price Checking**: Our app checks flight prices using the Amadeus flight search API.
-**Notifications**: Get notified via email, SMS, or WhatsApp when flight prices fall below the set threshold.
-**Easy Sign-Up**: Register to get notifications about cheap flights by filling out a simple Google Form.

## Architecture
Our project is built with Python and includes the following components:

1. **SpreadsheetManager**: Connects with the Google Spreadsheet API to manage/obtain destination and price threshold data.
2. **FlightSearchAPI**: Uses the Amadeus flight search API to fetch current flight prices.
3. **NotificationManager**: Handles sending notifications via email (using smtplib) and via SMS/WhatsApp (using Twilio).
4. **FlightDataManager**: Manages flight data, comparing current prices with our set thresholds.
