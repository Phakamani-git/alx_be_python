# Ask the user to input the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Generate reminder using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unknown priority level"

# Check time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority in ["high", "medium"]:
        message += ". Try to complete it soon."
    else:
        message += ". Consider completing it when you have free time."

# Print the final message
print(message)
