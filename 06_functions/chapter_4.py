def add_vat(price, vat_rate):
    return price + (price * (vat_rate / 100))


prices = [100, 200, 300]
vat_rate = 20

for price in prices:
    total = add_vat(price, vat_rate)
    print(f"Price: {price}, Total with VAT: {total}")