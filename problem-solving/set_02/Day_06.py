"""
 Challenge: JSON-to-Excel Converter Tool

Create a Python utility that reads structured data (like you'd get from an API) from a `.json` file and converts it to a CSV file that can be opened in Excel.

Your program should:
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Bonus:
- Provide feedback on how many records were converted
- Allow user to define which fields to extract
- Handle missing fields gracefully
"""

import json
import csv
import os

INPUT_FILE = "data.json"
OUTPUT_FILE = "converted_data.csv"

def load_json(input_file):
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        return []
    with open(input_file, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return []

def convert_to_csv(data, output_file):
    if not data:
        print("No data to convert.")
        return
    
    fieldnames = list(data[0].keys())
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            writer.writerow(record)
    print(f"Converted {len(data)} records to {output_file}.")

def main():
    print("Converting JSON to CSV....")
    data = load_json(INPUT_FILE)
    convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()