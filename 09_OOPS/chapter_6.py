class Order:
    def __init__(self, product):
        self.product = product
    
    def prepare(self):
        print(f"Preparing {self.product}")

class Shipping(Order): 
    def shipping(self):
        print("Adding shipping route")