def calculate_delivery_charge(distance: float) -> str:
    if distance <= 2:
        return "Delivery charge: 0"
    elif distance > 2 and distance <= 5:
        return "Delivery charge: 30"
    elif distance > 5 and distance <= 10:
        return "Delivery charge: 50"
    else:
        return "Delivery not available for your location."