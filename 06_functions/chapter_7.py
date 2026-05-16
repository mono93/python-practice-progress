order_type = "small"

def front_counter():
    def back_counter():
        global order_type
        order_type = "XXL"
    back_counter()

front_counter()
print(f"Output: {order_type}")