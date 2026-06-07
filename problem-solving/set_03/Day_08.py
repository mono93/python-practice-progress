import os
import csv
import requests
import schedule
import time
from datetime import datetime

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page':10,
    'page':1,
    'sparkline':False
}

CSV_FILE = 'crypto_prices.csv'

def fetch_and_save_crypto_data():
    try:
        response = requests.get(API_URL, params=PARAMS, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()  # Check if the request was successful
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return

    data = response.json()

    file_exists = os.path.isfile(CSV_FILE)


    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["timestamp", "coin", "current_price"])  # Write header if file doesn't exist

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for coin in data:
            writer.writerow([timestamp, coin['id'], coin['current_price']])
    print(f"✅ Data saved to {CSV_FILE}")

def job():
    print("Fetching data every day at 15:08...")
    fetch_and_save_crypto_data()

schedule.every().day.at("15:08").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)