from datetime import datetime

class BeverageOrder:
    # Class-level variables for tracking
    _id_counter = 0
    active_orders = []

    def __init__(self, drink_type, sweetness, size):
        if not OrderUtils.is_valid_size(size):
            raise ValueError(f"Invalid size: {size}")
            
        # Tracking metadata
        BeverageOrder._id_counter += 1
        self.order_id = BeverageOrder._id_counter
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Order details
        self.drink_type = drink_type
        self.sweetness = sweetness
        self.size = size
        
        # Log to active tracking list
        BeverageOrder.active_orders.append(self)

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["drink_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        drink_type, sweetness, size = order_string.split("-")
        return cls(drink_type, sweetness, size)
    
    @classmethod
    def get_total_orders(cls):
        return cls._id_counter

class OrderUtils:
    @staticmethod
    def is_valid_size(size):
        return size.strip().capitalize() in ["Small", "Medium", "Large"]


# --- Execution and Tracking Output ---

# 1. Validation check
print(f"Is 'Medium' valid? {OrderUtils.is_valid_size('Medium')}\n")

# 2. Creating generic beverage orders
order1 = BeverageOrder.from_dict({"drink_type": "Coffee", "sweetness": "Medium", "size": "Large"})
order2 = BeverageOrder.from_string("Matcha-Low-Small")
order3 = BeverageOrder("Smoothie", "Low", "Large")

# 3. View individual order tracking data
print("Order 1:", order1.__dict__)
print("Order 2:", order2.__dict__)
print("Order 3:", order3.__dict__)

# 4. View global tracking metrics
print(f"\nTotal orders processed: {BeverageOrder.get_total_orders()}")
print(f"Tracked Order IDs in system: {[o.order_id for o in BeverageOrder.active_orders]}")
