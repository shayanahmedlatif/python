# A small program helps you to calculate
# Tip based on user input, and divide them into each 
# Persons to calculate the results

# Ask the user for the bill amount
bill_amount = input("What is the total bill? \n$")
bill_amount_float = float(bill_amount)

# Ask the user for tip percentage
tip_amount = input("What percentage of tip would you like to give? \n")
tip_amount_float = float(tip_amount)

# Convert tip value
total_tip = (tip_amount_float / 100) * bill_amount_float
# total_tip = round(total_tip)
total_tip_two = float(f"{total_tip:.2f}")

# Add the total bill and tip amount
total_bill_to_pay = bill_amount_float + total_tip_two
total_bill_to_pay = float(f"{total_bill_to_pay:.2f}")

# Ask user to split the bill into x num of peoples
num_of_people = input(f"How many people will pay ${total_bill_to_pay}? \n")
# Divided the total bill into x number of people
divided_bill_amount = float(total_bill_to_pay )/ float(num_of_people)
divided_bill_amount = float(f"{divided_bill_amount:.2f}")

# Print the results on screen
print(f"Thanks! you've added ${total_tip_two} tip, and bill divided to {num_of_people} persons each ${divided_bill_amount}")