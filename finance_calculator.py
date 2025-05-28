try:
    # Prompt user for financial details
    income = float(input("Enter your monthly income: "))
    expenses = float(input("Enter your total monthly expenses: "))

    # Calculate monthly savings
    monthly_savings = income - expenses

    # Project annual savings with 5% interest using required formula
    projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

    # Display results
    print(f"Your monthly savings are ${monthly_savings:.2f}.")
    print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")

except ValueError:
    print("Please enter a valid number.")
