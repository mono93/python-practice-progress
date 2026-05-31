"""
Challenge: Set a Countdown Timer

Create a Python script that allows the user to set a timer in seconds. The script should:

1. Ask the user for the number of seconds to set the timer.
2. Show a live countdown in the terminal.
3. Notify the user when the timer ends with a final message and sound (if possible).

Bonus:
- Format the remaining time as MM:SS
- Use a beep sound (`\a`) at the end if the terminal supports it
- Prevent negative or non-integer inputs
"""

import time

def countdown_timer():
    seconds = input("Enter the number of seconds for the countdown timer: ")
    if not seconds.isdigit() or int(seconds) < 0:
        print("Please enter a valid non-negative integer.")
    else:
        seconds = int(seconds)
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer_format = f"{mins:02d}:{secs:02d}"
            print(timer_format, end="\r")
            time.sleep(1)
            seconds -= 1
        print("Time's up! \a")

countdown_timer()