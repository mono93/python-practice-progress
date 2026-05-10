# This function will be tested automatically. 
# Do not change the function name or parameter type.
def get_item_price(item: str) -> str:
    match item.lower():
        case "pizza":
            return "Price: 30 bucks"
        case "burger":
            return "Price: 15 bucks"
        case "pasta":
            return "Price: 20 bucks"
        case "salad":
            return "Price: 10 bucks"
        case _:
            return "Item not available"