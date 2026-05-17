def infinite_order():
    count = 1
    while True:
        yield f"Refill #{count}"
        count += 1


user1 = infinite_order()
for _ in range(10):
    print(next(user1))
