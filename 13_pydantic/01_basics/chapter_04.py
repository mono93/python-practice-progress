from typing import Optional
from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Monojit"
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=10000
    )
    personal_email: str = Field(
        ...,
        pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    )

employee_input = {"id": 1, "name":"Monojit", "salary": 13000, "personal_email": "monojit.saha@email.com"}
employee_1 = Employee(**employee_input)
print(employee_1)