def customer():
    print("Welcome")
    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

counter = customer()
next(counter)
counter.send("XL")
counter.send("XXL")
