class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def get_engine_info(self):
        return f"{self.horsepower} HP Engine"


class Vehicle:
    total_vehicles = 0

    def __init__(self, brand, model, engine, rental_price=0.0):
        self.brand = brand
        self.model = model
        self.engine = engine
        self._rental_price = rental_price
        Vehicle.total_vehicles += 1

    def get_details(self):
        return f"{self.brand} {self.model}, {self.engine.get_engine_info()}"

    @property
    def rental_price(self):
        return self._rental_price

    @rental_price.setter
    def rental_price(self, price):
        if price < 0:
            raise ValueError("Rental price cannot be negative")
        self._rental_price = price

    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles


# New Car Subclass
class Car(Vehicle):
    def __init__(self, brand, model, engine, seats, rental_price=0.0):
        super().__init__(brand, model, engine, rental_price)
        self.seats = seats

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details}, Seats: {self.seats}"
