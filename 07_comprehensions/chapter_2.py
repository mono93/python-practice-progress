sizes = [2, 4, 6, 8, 0, 1, 3, 5, 7, 9, 3, 1, 7, 5, 9]
even_set = {size for size in sizes if size % 2 != 0}
print(even_set)


nested_size = {
    1: [2, 4, 6, 8, 0],
    2: [1, 3, 5, 7, 9],
    3: [1, 2, 4, 5, 7]
}

unique_sizes = {x for xx in nested_size.values() for x in xx}

print(unique_sizes)
