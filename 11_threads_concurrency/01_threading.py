import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(3)

def serve_chai():
    for i in range(1, 4):
        print(f"Chai served for #{i}")
        time.sleep(4)
        
# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)
serve_thread = threading.Thread(target=serve_chai)

order_thread.start()
brew_thread.start()
serve_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()
serve_thread.join()

print("All orders taken and chai brewed")