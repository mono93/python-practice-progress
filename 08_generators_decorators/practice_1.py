"""
    Infinite generator that simulates a token dispenser.
    
    - Yields incrementing token numbers starting from `start`.
    - Accepts input via `send()` to optionally reset the counter to a new value.
    - Gracefully stops if `close()` is called.
"""

def token_dispenser(start: int = 1):
    current = start
    try:
        while True:
            received = yield current
            if received is not None:
                current = received
            else:
                current += 1
                
    except GeneratorExit:
        print("Dispenser closed.")

count = token_dispenser(10)
print(next(count))
print(next(count))
print(next(count))
print(count.send(50))
print(next(count))