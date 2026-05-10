amount = int(input("Enter the amount: "))

delivery_fees = 0 if amount > 300 else 30

print(f"total amount is {amount + delivery_fees}")