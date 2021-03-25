print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))

number_of_people = float(input("How many people to split the bill? "))

percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

bill_generated = total_bill/number_of_people

bill_generated_with_percentage = (bill_generated / 100) * percentage

print(f"Each person should pay:  ${round(bill_generated_with_percentage + bill_generated)}")