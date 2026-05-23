def process_order(item, quantity):
    try:
        price = {"widget": 20}[item]
        
        # Check if quantity is a number type
        if not isinstance(quantity, (int, float)):
            raise TypeError
            
        cost = price * quantity
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry, that item is not on the menu")
    except TypeError:
        print("Quantity must be a number")

process_order("gadget", 2)
process_order("widget", "two")
