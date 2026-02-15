"""
Author: Amanda Ruff
Date: February 15, 2026
File Name: Ruff_lemonadeStandSchedule.py
Description:
    This program manages a weekly schedule for a lemonade stand.
    It demonstrates the use of lists, for loops, and if/else
    conditionals to display tasks for each day of the week.
"""

# List of tasks related to running a lemonade stand
tasks = [
    "Buy lemons",
    "Make lemonade",
    "Sell lemonade",
    "Count earnings",
    "Clean up"
]

# Printing all tasks
print("Lemonade Stand Tasks:")
for task in tasks:
    print(f"- {task}")

print("\nWeekly Schedule:")

# List of days in the week
days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

# Index to track weekday tasks
task_index = 0

# Loop through each day and display the appropriate message
for day in days:
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: Day off — rest and recharge! 🛌")
    else:
        print(f"{day}: {tasks[task_index]}")
        task_index += 1
