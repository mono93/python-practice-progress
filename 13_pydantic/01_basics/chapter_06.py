from pydantic import BaseModel, Field, computed_field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    tarriff: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.tarriff
    


booking = Booking(
    user_id=1,
    room_id=1,
    nights=3,
    tarriff=1000
)

print(booking)
print(booking.model_dump())