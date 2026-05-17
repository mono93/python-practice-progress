def order():
    yield "SM"
    yield "MD"
    yield "LG"
    yield "XL"

def larger_order():
    yield "XXL"
    yield "XXXL"

def full_order():
    yield from order()
    yield from larger_order()

for o in full_order():
    print(o)
