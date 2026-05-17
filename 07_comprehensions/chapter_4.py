# Generator expression: Creates a blueprint; memory footprint stays tiny
gen_comp = (x for x in range(1000000))
print(next(gen_comp))
print(next(gen_comp))
print(next(gen_comp))
print(next(gen_comp))
print(next(gen_comp))


daily_sales = [2,4,6,8,0,1,3,5,7,9]
total_cups = (sale for sale in daily_sales if sale % 2 == 0)
print(next(total_cups))
print(total_cups)
print(sum(total_cups))
