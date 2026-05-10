def simulate_atm_withdrawals(balance: int, withdrawals: list[int]) -> list[str]:
    results = []
    index = 0

    while index < len(withdrawals):
        amount = withdrawals[index]
        if amount <= balance:
            balance -= amount
            results.append(f"Withdrawn: {amount}")
        else:
            results.append(f"Insufficient funds for requested amount: {amount}")
        index += 1

    results.append(f"Remaining Balance: {balance}")

    return results
