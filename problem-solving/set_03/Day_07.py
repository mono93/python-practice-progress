import os
import csv
import requests
from datetime import datetime
import matplotlib.pyplot as plt

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

def plot_graph(coin_id):
    times = []
    prices = []

    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["coin"] == coin_id:
                times.append(row['timestamp'])
                prices.append(float(row['current_price']))

    if not times:
        print(f"No data found for {coin_id}")
        return
    
    plt.figure(figsize=(10,5))
    plt.plot(times, prices, marker='o')
    plt.tight_layout()
    plt.grid()
    plt.show()

def display_csv_data():
    if not os.path.exists(CSV_FILE):
        print("No data found. Please run the script to fetch data first.")
        return

    with open(CSV_FILE, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['timestamp']} - {row['coin']}: ${row['current_price']}")


def main():
    print("Fetching live crypto data....")
    fetch_and_save_crypto_data()

    print("-" * 30)
    print("Displaying collected data:")
    display_csv_data()
    print("-" * 30)

    choice = input("Enter the coinname to get graph: ").strip().lower()

    if choice:
        plot_graph(choice)


if __name__ == "__main__":
    main()