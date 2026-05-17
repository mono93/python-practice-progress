from functools import wraps

def my_decorator(func):
    @wraps(func)
    def warpper():
        print("Before function call")
        func()
        print("After function call")
    return warpper

@my_decorator
def greet():
    print("Hello World")

greet()

# print(greet.__name__)
