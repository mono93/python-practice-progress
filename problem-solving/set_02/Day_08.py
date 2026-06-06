"""
Challenge : JSON Flattener

{
  "user": {
    "id": 1,
    "name": "Riya",
    "email": "riya@example.com",
    "address": {
      "city": "Delhi",
      "pincode": 110001
    }
  },
  "roles": ["admin", "editor"],
  "is_active": true
}

Flatten this to:

{
  "user.id": 1,
  "user.name": "Riya",
  "user.email": "riya@example.com",
  "user.address.city": "Delhi",
  "user.address.pincode": 110001,
  "roles.0": "admin",
  "roles.1": "editor",
  "is_active": true
}

"""

import json
import os

INPUT_FILE = 'input_data.json'
OUTPUT_FILE = 'flattened_data.json'

def flatten_json(data, parent_key='', separator='.'):
    items = {}

    if isinstance(data, dict):
        for key, value in data.items():
            full_key = f"{parent_key}{separator}{key}" if parent_key else key
            print(f"Processing dict key: {full_key}")
            items.update(flatten_json(value, full_key, separator))
    elif isinstance(data, list):
        for index, value in enumerate(data):
            full_key = f"{parent_key}{separator}{index}" if parent_key else str(index)
            print(f"Processing list index: {full_key}")
            items.update(flatten_json(value, full_key, separator))
    else:
        items[parent_key] = data
        print(f"Adding key-value pair: {parent_key}: {data}")

    return items


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: File '{INPUT_FILE}' does not exist.")
        return
    
    with open(INPUT_FILE, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    flattened_data = flatten_json(data)
    
    with open(OUTPUT_FILE, mode='w', encoding='utf-8') as json_file:
        json.dump(flattened_data, json_file, indent=4)

if __name__ == "__main__":
    main()

