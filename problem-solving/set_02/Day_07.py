"""
 Challenge: CSV-TO-JSON Converter Tool

"""

import csv
import json
import os

CSV_FILE = 'converted_data.csv'
JSON_FILE = 'data_1.json'

def load_csv(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return []
    
    with open(file_path, mode='r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        data = list(reader)
        return data

def convert_to_json(data, output_file):
    with open(output_file, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

def main():
    print(f"Loading data from {CSV_FILE}...")
    csv_data = load_csv(CSV_FILE)
    if not csv_data:
        print("Failed to load CSV data.")
        return
    
    convert_to_json(csv_data, JSON_FILE)

if __name__ == "__main__":
    main()

