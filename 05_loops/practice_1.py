def multiplication_table(number: int) -> list[str]:
    table = []
    for i in range(1, 11):
        result = number * i
        table.append(f"{number} x {i} = {result}")
    return table    
