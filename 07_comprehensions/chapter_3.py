old_dict = {'a': 1, 'b': 2, 'c': 3}
new_dict = {value: key for key, value in old_dict.items()}
print(new_dict)