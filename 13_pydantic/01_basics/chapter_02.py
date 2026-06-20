from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_1 = Product(id=1, name="laptop", price=10.99)
product_2 = Product(id=2, name="monitor", price=11.99, in_stock=True)

print(product_1)
print(product_2)
