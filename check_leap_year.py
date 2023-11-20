# Which year do you want to check?
year = int(input("What year you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Check the divisible function

check_year_four = year % 4
check_year_hundered = year % 100
check_year_four_hundered = year % 400

if check_year_four == 0 and check_year_hundered != 0:
  print("Leap year")
elif check_year_four_hundered == 0:
  print("Leap year")
else:
  print("Not leap year")

