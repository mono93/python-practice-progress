def pure_add(a, b):
    return a+b


count = 0


def impure_increment():
    global count
    count += 1
    return count


def factorial_recursive(n):
    if n <= 1:
        return 1

    return factorial_recursive(n-1) * n

def square_list(nums):
    return list(map(lambda num: num ** 2, nums))
