sizes = [10, 20, 30, 40, 50]

print(sizes[2])  # This will print 30

try:
    print(sizes[5])  # This will raise an IndexError since there is no index
except IndexError:
    print("IndexError: The index is out of range.")
finally:
    print("This block will always execute, regardless of whether an exception occurred or not.")


def process_score(score: float) -> str:
    """Validates input range and returns the letter grade."""
    try:
        # Check boundary condition
        if not (0 <= score <= 100):
            raise ValueError(f"Score {score} is out of bounds (0-100).")
    except ValueError as error:
        # Catch and pass the error back to the caller
        raise error
    else:
        # This executes ONLY if no exception was thrown
        if score >= 90: return "A"
        if score >= 80: return "B"
        if score >= 70: return "C"
        if score >= 60: return "D"
        return "F"

def run_grading_system(student_name: str, score: float) -> None:
    """Controls the program execution lifecycle."""
    try:
        print(f"Evaluating {student_name}...")
        grade = process_score(score)
    except ValueError as error:
        print(f"System Error: {error}")
    else:
        print(f"Result: {student_name} received a grade of {grade}.")
    finally:
        print("Session closed. Next entry ready.\n" + "-"*35)

# Execution Examples
run_grading_system("Alex", 85)
run_grading_system("Sam", 120)