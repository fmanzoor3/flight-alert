# FlightAlert

## Project Overview
FlightAlert is here to help you find and be notified about affordable flights. Sign up to receive alerts when flight prices to popular destinations drop below a certain price. This project integrates various APIs to make everything work seamlessly.

## Features
- **Popular Destinations and Price Limits**: We track popular destinations and their affordable-price threshold using a Google Spreadsheet.
- **Flight Price Checking**: Our app checks flight prices using the Amadeus flight search API.
- **Notifications**: Get notified via email, SMS, or WhatsApp when flight prices fall below the set threshold.
- **Easy Sign-Up**: Register to get notifications about cheap flights by filling out a simple Google Form.

## Architecture
Our project is built with Python and includes the following components:

1. **SpreadsheetManager**: Connects with the Google Spreadsheet API to manage/obtain destination and price threshold data.
2. **FlightSearchAPI**: Uses the Amadeus flight search API to fetch current flight prices.
3. **NotificationManager**: Handles sending notifications via email (using smtplib) and via SMS/WhatsApp (using Twilio).
4. **FlightDataManager**: Manages flight data, comparing current prices with our set thresholds.

## Installation

1. Clone the repository: 
    ```bash
    git clone https://github.com/fmanzoor3/flight-alert.git
    cd flight-alert
    ```

2. Install the required dependencies: 
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your environment variables in a `.env` file in the root directory:
    ```plaintext
    SHEET_AUTHENTICATION_TOKEN=your_sheet_authentication_token
    SHEETY_USERNAME=your_sheety_username
    SHEETY_PASSWORD=your_sheety_password
    SHEETY_PRICES_ENDPOINT=your_sheety_prices_endpoint
    SHEETY_USERS_ENDPOINT=your_sheety_users_endpoint

    AMADEUS_API_KEY=your_amadeus_api_key
    AMADEUS_SECRET=your_amadeus_secret

    TWILIO_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_VIRTUAL_NUMBER=your_twilio_virtual_number
    TWILIO_VERIFIED_NUMBER=your_twilio_verified_number
    TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number

    EMAIL_PROVIDER_SMTP_ADDRESS=smtp.your-email-provider.com
    MY_EMAIL=your_email_address
    MY_EMAIL_PASSWORD=your_email_password
    ```

4. Run the application: 
    ```bash
    python main.py
    ```

## Usage

1. **Register Users:** Want to get notified about cheap flights? Just fill out this Google Form with your name and email address. [Sign up here](https://docs.google.com/forms/d/e/1FAIpQLSdcf9XQDRiVge1LFUbGzEqsGe1TifiLMvEL46yM5-DV_6mYaw/viewform?usp=sf_link).

2. **Manage Destinations and Price Limits:** We’ve got a list of popular destinations and their price limits in a Google Spreadsheet. The app regularly checks these prices and sends notifications when they go below the limits.

   ![Spreadsheet Example](path_to_screenshot.png)

3. **Receive Notifications:** When flight prices drop below the threshold, you’ll get a notification with all the details via email.

## Acknowledgements

- [Google Sheets API](https://developers.google.com/sheets/api)
- [Amadeus Flight Search API](https://developers.amadeus.com)
- [Twilio API](https://www.twilio.com/docs/usage/api)
- [SMTP Library](https://docs.python.org/3/library/smtplib.html)
