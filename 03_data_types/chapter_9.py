foreign_cars = {"audi", "bmw", "subaru", "toyota", "land rover"}
indian_cars = {"tata", "mahindra", "maruti", "honda", "land rover"}

# Union of two sets
all_cars = foreign_cars | indian_cars
print("All cars:", all_cars)

# Intersection of two sets
common_cars = foreign_cars & indian_cars
print("Common cars:", common_cars)

only_foreign_cars = foreign_cars - indian_cars
print("Only foreign cars:", only_foreign_cars)

only_indian_cars = indian_cars - foreign_cars
print("Only Indian cars:", only_indian_cars)

# membership testing
print("Is 'audi' a foreign car?", "audi" in foreign_cars)
print("Is 'tata' a foreign car?", "tata" in foreign_cars)
print("Is 'Tata' an Indian car?", "tata" in indian_cars)

frozen_cars = frozenset(foreign_cars)
print("Frozen cars:", frozen_cars)

frozen_cars.add("mercedes")  # This will raise an error since frozenset is immutable