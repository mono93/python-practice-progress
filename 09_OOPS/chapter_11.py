class Student:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        # Returns the actual age without modification
        return self._age
    
    @age.setter
    def age(self, age):
        # Validates typical school-age range
        if 5 <= age <= 18:
            self._age = age
        else:
            raise ValueError("Student age must be between 5 and 18 years")
        
# Example usage:
student = Student(10)
print(student.age)  # Output: 10

try:
    student.age = 19 # This will trigger the validation error
    print(student.age)  
except ValueError as e:
    print(e)  # Output: Student age must be between 5 and 18 years
