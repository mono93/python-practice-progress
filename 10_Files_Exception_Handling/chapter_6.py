class InvalidItemError(Exception): 
    pass

def calculate_total(item_type, quantity):
    catalog = {"standard": 20, "premium": 40}
    try:
        if item_type not in catalog:
            raise InvalidItemError("That item is not available")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        total = catalog[item_type] * quantity
        print(f"Total for {quantity} units of {item_type}: {total}")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Process execution finalized.")

calculate_total("custom", 2)
calculate_total("standard", "three")
calculate_total("premium", 3)
