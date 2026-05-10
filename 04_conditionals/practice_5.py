# This function will be tested automatically. 
# Do not change the function name or parameter type.
def verify_age(age_str: str) -> str:
    age = int(age_str)
    access = "Access granted" if age >= 18 else "Access denied"
    return access