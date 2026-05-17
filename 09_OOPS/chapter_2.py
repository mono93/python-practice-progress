class Car:
    manufacturer = "Italy" 

print(Car.manufacturer)

Car.is_sport = True
print(Car.is_sport)

# creating objects from class chai

print("############################")

lamborghini = Car()
lamborghini.is_sport = False
print(lamborghini.manufacturer)
print(lamborghini.is_sport)
lamborghini.is_v12 = True

# print(Car.is_v12)

