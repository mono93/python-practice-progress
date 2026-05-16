loyalty_points = 0

def process_transactions(transactions: list[int]):
    total = 0
    for transaction in transactions:
        total += transaction
    
    def apply_bonus():
        nonlocal total
        if total > 1000:
            total += 50 

    global loyalty_points
    loyalty_points += total // 100

    apply_bonus()
    
    return total
    