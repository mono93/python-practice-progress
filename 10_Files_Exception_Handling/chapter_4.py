def process_item(item_type):
    if item_type not in ["standard", "premium", "deluxe"]:
        raise ValueError("Unsupported type...")
    print(f"Processing {item_type} item...")

try:
    process_item("custom")
except ValueError as e:
    print(e)
