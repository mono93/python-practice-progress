values = [1, 2, 3, 4, 5]
print(f"Original list: {values}")
print(f"List length: {len(values)}")
print(f"id of the list: {id(values)}")
values.append(6)
print(f"Updated list: {values}")
print(f"Updated list length: {len(values)}")
print(f"id of the updated list: {id(values)}")
values.insert(0, 0)
print(f"List after inserting 0 at index 0: {values}")
print(f"id of the list after insertion: {id(values)}")  
values.remove(3)
print(f"List after removing 3: {values}")
print(f"id of the list after removal: {id(values)}")

values1 = [1, 2, 3]
values2 = [4, 5, 6]
values1.extend(values2)
print(f"Extended list: {values1}")

values.insert(3, 3)
print(f"List after inserting 3 at index 3: {values}")
print(f"id of the list after inserting 3: {id(values)}")

values.reverse()
print(f"Reversed list: {values}")
print(f"id of the list after reversing: {id(values)}")

values.reverse()

last_value = values.pop()
print(f"Popped value: {last_value}")
print(f"List after popping last value: {values}")
print(f"id of the list after popping: {id(values)}")

max_value = max(values)
print(f"Maximum value in the list: {max_value}")
min_value = min(values)
print(f"Minimum value in the list: {min_value}")
values.sort()
print(f"Sorted list: {values}")
print(f"id of the sorted list: {id(values)}")

value1 = [1, 2, 3]
value2 = [4,5]
value3 = value1 + value2
print(f"Concatenated list: {value3}")
print(f"id of the concatenated list: {id(value3)}")

# from operator import itemgetter
# values = [5, 2, 9, 1, 5, 6]
# sorted_values = sorted(values)
# print(f"Sorted list: {sorted_values}")
# print(f"id of the sorted list: {id(sorted_values)}")

text1 = "Hello"
text2 = " World"
raw_text = bytearray(text1, "utf-8")
raw_text.append(33)  # Append '!' character
print(f"Raw text as bytearray: {raw_text}")
decoded_text = raw_text.decode("utf-8")
print(f"Decoded text: {decoded_text}")

raw_text.extend(text2.encode("utf-8"))
print(f"Raw text after appending text2: {raw_text}")
decoded_text = raw_text.decode("utf-8")
print(f"Decoded text after appending text2: {decoded_text}")
