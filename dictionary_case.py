users = [
    {"id": 1, "total": 130, "coupon": "P20"},
    {"id": 2, "total": 125, "coupon": "P15"},
    {"id": 3, "total": 135, "coupon": "P10"},
]

discounts = {
    "P20": (0.20, 0),
    "P15": (0.15, 0),
    "P10": (0, 10),
}

for user in users:
    percentage_discount, fixed_discount = discounts.get(user["coupon"], (0, 0))
    total = user["total"]
    total_after_percentage = total * (1 - percentage_discount)
    final_total = total_after_percentage - fixed_discount
    print(f"User {user['id']} final total: {final_total}")