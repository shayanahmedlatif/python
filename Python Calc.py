
import math

# Defining calculation functions

def addition(number_1, number_2):
    # Adding two numbers
    final_results = number_1 + number_2
    return final_results
def subtraction(number_1, number_2):
    # Subtracting two numbers
    final_results = number_1 - number_2
    return final_results
def multiplication(number_1, number_2):
    # Subtracting two numbers
    final_results = number_1 * number_2
    return final_results
def division(number_1, number_2):
    # Subtracting two numbers
    if number_2 != 0:
        final_results = number_1 / number_2
    else:
        print("Division by zero impossible.")
    return final_results

# Function to check the input validation against number.
# All operation
all_operations = {

    "addition": ["addition", "add", "+"],
    "subtraction": ["subtraction", "subtract", "-"],
    "multiplication": ["multiplication", "multiply", "*"],
    "division": ["division", "divide", "/"]
}

# Program start here.
# Printing symbols on the screen.
print("Welcome to the Python Calculator.")
for operation_id, operations in all_operations.items():
    print(f"{operation_id}")
# Setting a condition for while loop

# Program starts here.
final_results = None
continue_calculation = True
while continue_calculation:

    if final_results is None:
        ask_user = input("Which operation would you like to perform? ").lower()
    else:
        ask_user = input("What another calculation woudld you like to perform? ")

    selected_operation = None
    for operation_id, operations in all_operations.items():
        if ask_user in operations:
            selected_operation = operation_id
            break
    else:
        print("There is no such function. Try again.")
        continue

    if final_results is None:
        while True:
            try:
                number_1 = math.ceil(float(input("Enter your first number: ")))
                break
            except ValueError:
                print("Invalid number, try again.")
                continue
        while True:
            try:
                number_2 = math.ceil(float(input("Enter your second number: ")))
                break
            except ValueError:
                print("Invalid number, try again.")
                continue
    else:
        print("We'll use previouse results.")
        number_1 = final_results
        while True:
            try:
                number_2 = math.ceil(float(input("Enter your second number: ")))
                break
            except ValueError:
                print("Invalid number, try again.")
                continue
    if selected_operation in ["addition", "add", "+"]:
        final_results = addition(number_1, number_2)
    elif selected_operation in ["subtraction", "subtract", "-"]:
        final_results = subtraction(number_1, number_2)
    elif selected_operation in ["multiplication", "multiply", "*"]:
        final_results = multiplication(number_1, number_2)
    elif selected_operation in ["division", "divide", "/"]:
        final_results = division(number_1, number_2)
    print(f"{operation_id} of {number_1} and {number_2} is {final_results}.")

    if input("Do you want to continue calculation? Y/N").lower() not in ["yes", "y"]:
        print("Thank you. Goodbye.")
        continue_calculation = False
    else:
        continue_calculation = True