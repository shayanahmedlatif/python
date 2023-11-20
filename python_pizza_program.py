print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? ") # What size pizza do you want? S, M, or L
add_pepperoni = input("DO you want peperoni? ") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? ") # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

# Price Menu

# Pizza Prices

small = int(15)
medium = int(20) 
large = int(25)
# Peperoni Prices

pep_yes = int(2)
pep_yes_ml = int(3) 
pep_no = int(0)
# Extra Cheese Prices

cheesee_yes = int(1) 
cheesee_no = int(0)

# Total price formula
total_price = int(0)

if size == "S":
    total_price = total_price + int(small)
if size == "M":
    total_price = total_price + int(medium)
if size == "L":
    total_price = total_price + int(large)

if add_pepperoni == "Y" and size == "S":
    total_price = total_price + pep_yes
if add_pepperoni == "Y" and size == "M":
    total_price = total_price + pep_yes_ml
if add_pepperoni == "Y" and size == "L":
    total_price = total_price + pep_yes_ml
elif add_pepperoni == "N":
    total_price = total_price + pep_no
if extra_cheese == "Y":
    total_price = total_price + cheesee_yes
    print(f"Your final bill is: ${total_price}.")
elif extra_cheese == "N":
    total_price = total_price + cheesee_no
    print(f"Your final bill is: ${total_price}.")