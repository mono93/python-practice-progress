# ==========================================
# 1. THE BASE CLASS
# ==========================================
class CustomerOrder:
    def __init__(self, item_name):
        self.item_name = item_name
    
    def process_billing(self):
        print(f"Processing billing for: {self.item_name}")


# ==========================================
# 2. INHERITANCE ("Is-A" Relationship)
# ShippedOrder IS A specialized type of CustomerOrder.
# ==========================================
class ShippedOrder(CustomerOrder): 
    def __init__(self, item_name, tracking_number="STD-123"):
        super().__init__(item_name)  # Pass data up to parent constructor
        self.tracking_number = tracking_number
        
    def assign_shipping_route(self):
        print(f"Route assigned for {self.item_name} (ID: {self.tracking_number})")


# ==========================================
# 3. INSTANCE COMPOSITION ("Has-A" Relationship)
# UrgentDeliveryService HAS A ShippedOrder instance hardcoded inside it.
# ==========================================
class UrgentDeliveryService:
    def __init__(self, urgent_item_name, priority_level):
        # Directly creating a ShippedOrder object during initialization
        self.base_order = ShippedOrder(urgent_item_name, tracking_number="EXP-999")
        self.priority_level = priority_level

    def dispatch_immediately(self):
        print(f"Priority {self.priority_level} dispatch triggered!")
        self.base_order.assign_shipping_route()


# ==========================================
# 4. CLASS-LEVEL COMPOSITION / FACTORY PATTERN
# DispatchManager holds a SWAPPABLE class blueprint as a class variable.
# ==========================================
class DispatchManager:
    # Class variable blueprint. Tells the class WHICH type of object to build.
    order_blueprint = CustomerOrder

    def __init__(self, item_name):
        # Dynamically instantiates whatever class is currently assigned to the blueprint
        self.active_order = self.order_blueprint(item_name)

    def dispatch(self):
        # Resolves the 'product.product' syntax issue with clean variable names
        print(f"Dispatching order details: {self.active_order.item_name}")


# ==========================================
# 5. EXECUTION & TEACHING DEMONSTRATION
# ==========================================

print("=== 1. TESTING INHERITANCE ===")
standard_order = ShippedOrder("Laptop", "STD-123")
standard_order.process_billing()       # Inherited from parent
standard_order.assign_shipping_route() # Unique to child


print("\n=== 2. TESTING INSTANCE COMPOSITION ===")
express_service = UrgentDeliveryService("Medical Kit", priority_level="High")
express_service.base_order.process_billing() # Accessing parent via the composed object
express_service.dispatch_immediately()        # Executing composition logic


print("\n=== 3. TESTING DYNAMIC FACTORY PATTERN ===")
print("[Step A: Default Blueprint]")
manager_one = DispatchManager("Standard Textbook")
manager_one.active_order.process_billing()   # Runs CustomerOrder logic
manager_one.dispatch()

print("\n[Step B: Swapped Blueprint]")
# Dynamically change the blueprint class at runtime for teaching flexibility
DispatchManager.order_blueprint = ShippedOrder

manager_two = DispatchManager("Premium Smartphone")
manager_two.active_order.process_billing()      # Inherited method still works
manager_two.active_order.assign_shipping_route() # New child-specific method is now available!
manager_two.dispatch()
