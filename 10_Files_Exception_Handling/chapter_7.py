# file = open("order.txt", "w")
# try:
#     file.write("XXL Shirt - 2")
# finally:
#     file.close()


with open("order.txt", "w") as file:
    file.write("XXL Shirt - 2")
