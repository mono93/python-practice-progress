class Car:
    manufacturer = "Italy"
    is_sport = True
    is_v12 = True

bmv = Car()
print(bmv.is_sport)

bmv.is_sport = False
bmv.is_hyper = True
print(bmv.is_sport)
print(bmv.is_hyper)

del bmv.is_sport
del bmv.is_hyper


print(bmv.is_sport)
print(bmv.is_hyper)
