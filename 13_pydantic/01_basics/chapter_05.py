from pydantic import BaseModel, field_validator, model_validator, ValidationError
from typing import Optional

class UserRegistration(BaseModel):
    username: str
    password: str
    confirm_password: str
    age: int

    # 1. FIELD VALIDATOR (Validates a single field)
    @field_validator("username")
    @classmethod
    def validate_username(cls, value: str) -> str:
        """Ensures the username has no spaces and is alphanumeric."""
        if not value.isalnum():
            raise ValueError("Username must be alphanumeric (letters and numbers only)")
        return value.lower()  # You can also normalize/modify the data

    @field_validator("age")
    @classmethod
    def check_age(cls, value: int) -> int:
        """Ensures the user meets a minimum age requirement."""
        if value < 18:
            raise ValueError("You must be at least 18 years old to register")
        return value

    # 2. MODEL VALIDATOR (Validates multiple fields together / entire model)
    @model_validator(mode="after")
    def verify_password_match(self) -> "UserRegistration":
        """Ensures that the password and confirm_password fields match perfectly."""
        # mode="after" gives you access to the instantiated object via 'self'
        if self.password != self.confirm_password:
            raise ValueError("The two passwords do not match")
        return self


# ==========================================
# TESTING THE CODE
# ==========================================

print("--- Test Case 1: Valid Data ---")
try:
    valid_user = UserRegistration(
        username="JohnDoe123",
        password="securePassword!",
        confirm_password="securePassword!",
        age=25
    )
    print(f"Success! Registered User: {valid_user.model_dump()}")
except ValidationError as e:
    print(e)


print("\n--- Test Case 2: Field Validator Fails ---")
try:
    invalid_field_user = UserRegistration(
        username="john doe",  # Contains a space (Fails field_validator)
        password="password123",
        confirm_password="password123",
        age=16                # Underage (Fails field_validator)
    )
except ValidationError as e:
    print(e)


print("\n--- Test Case 3: Model Validator Fails ---")
try:
    invalid_model_user = UserRegistration(
        username="ValidUser7",
        password="secretpassword",
        confirm_password="differentpassword",  # Mismatched (Fails model_validator)
        age=30
    )
except ValidationError as e:
    print(e)
