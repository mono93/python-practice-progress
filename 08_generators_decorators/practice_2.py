from functools import wraps

def cache_results(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = (args, tuple(sorted(kwargs.items())))
        
        if cache_key in cache:
            return f"From Cache: {cache[cache_key]}"
        else:
            result = func(*args, **kwargs)
            cache[cache_key] = result
            return f"Computed: {result}"
            
    return wrapper

@cache_results
def multiply(a: int, b: int) -> int:
    return a * b

multiply(7,6)
multiply(7,6)
