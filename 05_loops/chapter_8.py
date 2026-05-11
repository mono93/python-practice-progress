staff = [("John", 30), ("Jane", 25), ("Emily", 35)]

for name, age in staff:
    if age > 25:
        print(f"{name} is eligible for the junior position.")
        break
else:
    print("All staff members have been processed.")
