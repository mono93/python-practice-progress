def create_order(product, size="L"):
    print(f"Dispatching: {product} of size {size}")

def create_order_1(*args, **kwargs):
    print(f"{args}")
    print(f"{kwargs}")

create_order("Shirt", "XL");
create_order(size="XL", product="Tshirt")

create_order_1("a", "b", "c", check="yes")