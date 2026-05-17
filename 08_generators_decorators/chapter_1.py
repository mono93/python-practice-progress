def serve_order():
    yield 'sm'
    yield 'md'
    yield 'lg'
    yield 'xl'

orders = serve_order()

# for order in orders: 
#     print(order)

# alternate method
print(next(orders))
print(next(orders))
print(next(orders))
print(next(orders))