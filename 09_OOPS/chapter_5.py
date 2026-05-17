class Order:
    def __init__(self, product, size):
        self.product = product
        self.size = size

    def show(self):
        return f"{self.product} -> {self.size}"
    

o1 = Order("Tshirt", "XXL")
print(o1.show())