"""
 Challenge: Minutes Alive Calculator

Write a Python script that calculates approximately how many minutes old a person is, based on their age in years.

Your program should:
1. Ask the user for their age in years (accept float values too).
2. Convert that age into:
   - Total days
   - Total hours
   - Total minutes
3. Display the result in a readable format.

Assumptions:
- You can use 365.25 days/year to account for leap years.
- You don't need to handle time zones or exact birthdates in this version.

Example:
Input:
  Age: 25

Output:
  You are approximately:
    - 9,131 days old
    - 219,144 hours old
    - 13,148,640 minutes old

Bonus:
- Add comma formatting for large numbers
- Let the user try again without restarting the program
"""

def calculate_minutes_alive(age_years):

    DAY_IN_YEAR = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    days = age_years * DAY_IN_YEAR
    hours = days * HOURS_IN_DAY
    minutes = hours * MINUTES_IN_HOUR
    return round(days), round(hours), round(minutes)

while True:
    try:
        age_input = input("Enter your age in years (or type 'exit' to quit): ").strip()
        if age_input.lower() == 'exit':
            print("Goodbye!")
            break
        age_years = float(age_input)
        days, hours, minutes = calculate_minutes_alive(age_years)
        print("\nYou are approximately:")
        print(f"  - {days:,.0f} days old")
        print(f"  - {hours:,.0f} hours old")
        print(f"  - {minutes:,.0f} minutes old")
    except ValueError:
        print("Please enter a valid number for age or type 'exit' to quit.")
