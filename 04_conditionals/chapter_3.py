order_catelog = {"small": 10, "medium": 15, "large": 20}
order_size = input("Enter the size of your order: ").lower();
INVALID_ORDER_MSG = "Invalid order size. Please choose from small, medium, or large."

# method 1
if order_size in order_catelog:
    print(f"The price of a {order_size} order is: {order_catelog[order_size]}")
else:
    print(INVALID_ORDER_MSG)

# method 2
if order_size == "small":
    print(f"The price of a {order_size} order is: {order_catelog[order_size]}")
elif order_size == "medium":
    print(f"The price of a {order_size} order is: {order_catelog[order_size]}")
elif order_size == "large":
    print(f"The price of a {order_size} order is: {order_catelog[order_size]}")
else:
    print(INVALID_ORDER_MSG)

# method 3
match order_size:
    case "small":
        print(f"The price of a {order_size} order is: {order_catelog[order_size]}")
    case "medium":
        print(f"The price of a {order_size} order is: {order_catelog[order_size]}")
    case "large":
        print(f"The price of a {order_size} order is: {order_catelog[order_size]}")
    case _:
        print(INVALID_ORDER_MSG)


