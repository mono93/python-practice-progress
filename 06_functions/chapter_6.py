def update_order():
    order_type = "XXl"
    def counter():
        nonlocal order_type
        order_type = "xl"
    counter()
    print(f" order type {order_type}")

update_order()