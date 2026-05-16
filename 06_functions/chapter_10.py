count = 10


def pure_function(order):
    return order + 5


def impure_function(order):
    global count
    count += order


print(f"Value from pure function {pure_function(100)}")
print(f"Before impure function {count}")
impure_function(100)
print(f"After impure function {count}")


def recursive_fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1

    memo[n] = recursive_fibonacci(n-1, memo) + recursive_fibonacci(n-2, memo)
    return memo[n]


print(recursive_fibonacci(5))


orders = [2, 5, 3, 4, 1]
print(list(map(lambda order: order+1, orders)))
print(list(filter(lambda order: order > 3, orders)))
