# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to print each row
while row < size:
    # Use for loop to print each asterisk in the row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
