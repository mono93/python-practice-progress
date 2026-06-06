"""
 Challenge: Real-Time Weather Logger (API + CSV)

Build a Python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking.

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API.
3. Store the following in a CSV file (`weather_log.csv`):
   - Date (auto-filled as today's date)
   - City
   - Temperature (in °C)
   - Weather condition (e.g., Clear, Rain)
4. Prevent duplicate entries for the same city on the same day.
5. Allow users to:
   - Add new weather log
   - View all logs
   - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
- Handle API failures and invalid city names gracefully
"""

import os
import csv
from datetime import datetime
import requests

FILE_NAME = "weather_log.csv"
API_KEY = "your api key"  # Replace with your OpenWeatherMap API key
URL = f"https://api.openweathermap.org/data/2.5/weather?&appid={API_KEY}&units=metric"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "City", "Temperature (°C)", "Weather Condition"])

def log_wheather():
   city = input("Enter your city name: ")
   date_time = datetime.now().strftime("%Y-%m-%d")

   with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.DictReader(file)
      for row in reader:
         if row["City"].lower() == city.lower() and row["Date"] == date_time:
            print(f"Weather data for {city} on {date_time} already exists.")
            return

   try:
      response = requests.get(URL + f"&q={city}")
      data = response.json()

      if response.status_code != 200:
         print(f"Error fetching data: {data.get('message', 'Unknown error')}")
         return
      
      temperature = data['main']['temp']
      weather_condition = data['weather'][0]['main']

      with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
         writer = csv.writer(file)
         writer.writerow([date_time, city, temperature, weather_condition])
         print(f"Weather data for {city} on {date_time} logged successfully.")

   except Exception:
       print("Failed to make API call")

def view_logs():
   with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
      reader = csv.reader(file)
      for row in reader:
         print(row)

def main():
   while True:
      print("\n1. Add new weather log")
      print("2. View all logs")
      print("3. Exit")
      choice = input("Enter your choice: ")

      if choice == '1':
         log_wheather()
      elif choice == '2':
         view_logs()
      elif choice == '3':
         break
      else:
         print("Invalid choice. Please try again.")

main()
   