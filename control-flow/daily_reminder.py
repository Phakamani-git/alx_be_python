# Ask the user to input the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Use match-case to handle priority
match priority:
    case "high":
        base_message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        base_message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        base_message = f"Note: '{task}' is a low priority task"
    case _:
        base_message = f"Note: '{task}' has an unknown priority level"

# Modify message based on time sensitivity
if time_bound == "yes":
    if priority in ["high", "medium"]:
        print(f"{base_message} that requires immediate attention today!")
    else:
        print(f"{base_message} that requires immediate attention today!")
else:
    if priority in ["high", "medium"]:
        print(f"{base_message}. Try to complete it soon.")
    else:
        print(f"{base_message}. Consider completing it when you have free time.")
