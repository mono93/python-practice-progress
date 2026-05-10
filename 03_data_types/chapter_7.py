values = (1, 2, 3)
print(f"Values: {values}")
print(f"Values id: {id(values)}")

# values.add(4) # This will raise an error since tuples are immutable

values += (4, 5)
print(f"Updated values: {values}")
print(f"Updated values id: {id(values)}")

(a, b, c, d, e) = values
print(f"a: {a}, b: {b}, c: {c}, d: {d}, e: {e}")

value1, value2 = 10, 20
print(f"value1: {value1}, value2: {value2}")
value1, value2 = value2, value1
print(f"After swapping - value1: {value1}, value2: {value2}")

# membership test
print(2 in values)
print(10 in values)
print(5 in values)