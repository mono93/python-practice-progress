# This function will be tested automatically.
# Do not change the function name or parameters.


"""
    items: A list of dictionaries, each representing a product with keys:
        - "name": str
        - "price": int
        - "category": str
    
    Returns:
        - List of names of affordable products (price < 500)
        - Set of unique categories
        - Dictionary of product name to price mapping
        - Generator expression converted to list of prices after applying 10% discount
"""

def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:    
    affordable_products = [item["name"] for item in items if item["price"] < 500]
    unique_category = {item["category"] for item in items}
    name_to_price_mapping = {item["name"]: item["price"] for item in items}
    dicounted_price = list(int(item["price"] * 0.9) for item in items)
    
    return (affordable_products, unique_category, name_to_price_mapping, dicounted_price)