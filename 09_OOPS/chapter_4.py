class Car:
    manufacturer = "Italy"
    def show(self):
        return f"######## - {self.manufacturer}"

bmw = Car()
print(bmw.show())
print(Car.show(bmw))