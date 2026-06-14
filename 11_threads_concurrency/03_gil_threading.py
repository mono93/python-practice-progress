import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

thread1 = threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")
thread3 = threading.Thread(target=brew_chai, name="Barista-3")

start = time.time()
thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
end = time.time()

print(f"total time taken: {end - start:.2f} seconds")
