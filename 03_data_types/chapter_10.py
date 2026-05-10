order = {"type": "books", "size": "Large", "price": 100}
print(order["type"]);
print(order["size"]);
print(order["price"]);


order1 = {}
order1["type1"] = "pens"
order1["size"] = "Medium"
order1["price"] = 50

print(order1["type1"]);
print(order1["size"]);
print(order1["price"]);

del order1["size"]
print(order1)

print("size" in order1)
print(order1.keys())
print(order1.values())
print(order1.items())

print(order1.get("type1"))
print(order1.get("price", "price not found"))


last_item = order1.popitem()
print(last_item)

print(order1)

print(order)
order.update(order1)
print(order)

print(order.get("size", "size not found"))