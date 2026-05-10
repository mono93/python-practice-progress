device_status = "inactive"
temperature = 25

if device_status == "active":
    if temperature > 35:
        print("Warn: High temperature!")
    else:
        print("Temperature normal")
else:
    print("Device is offline.")