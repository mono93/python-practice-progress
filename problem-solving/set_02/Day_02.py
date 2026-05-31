"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_student_data():
    students = []

    while True:
        name = input("Enter name of the student (or 'done' to finish): ").strip()

        if name.lower() == 'done':
            break

        matchs = [student for student in students if student['name'].lower() == name.lower()]

        if matchs:
            print("Student name already exists. Please enter a unique name.")
            continue

        try:
            marks = int(input("Enter marks for the student: ").strip())
        except ValueError:
            print("Invalid input for marks. Please enter an integer.")

        students.append({'name': name, 'marks': marks})
    return students

def analyze_marks(students):
    if not students:
        print("No student data to analyze.")
        return

    total_students = len(students)
    total_marks = sum(student['marks'] for student in students)
    average_marks = total_marks / total_students

    highest_marks = max(student['marks'] for student in students)
    lowest_marks = min(student['marks'] for student in students)

    highest_scorers = [student['name'] for student in students if student['marks'] == highest_marks]
    lowest_scorers = [student['name'] for student in students if student['marks'] == lowest_marks]

    print("\nStudent Marks Report")
    print("--------------------")
    print(f"Total number of students: {total_students}")
    print(f"Average marks: {average_marks:.2f}")
    print(f"Highest marks: {highest_marks} - Scored by: {', '.join(highest_scorers)}")
    print(f"Lowest marks: {lowest_marks} - Scored by: {', '.join(lowest_scorers)}")


students_data = collect_student_data()
analyze_marks(students_data)

