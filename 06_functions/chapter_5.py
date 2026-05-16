def serve_order():
    order_type = "Large"
    print(f"Inside function {order_type}")

order_type = "Medium"
serve_order()
print(f"Outside function {order_type}")

def f1():
    order_type = "xl"
    def print_order():
        order_type = "xxl"
        print(f"Inner: {order_type}")

    print(f"Outer: {order_type}")
    print_order()   

f1()     