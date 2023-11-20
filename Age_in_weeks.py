# This small piece of code will tell the user
# Life's weeks left into their age if they live until 90 years.

# 90 years into weeks
max_life_in_weeks = 90 * 52

# Ask user's age in Years and converts years into weeks
user_age = int(input("What is your age: "))
user_age_in_weeks = user_age * 52

# Calculate the weeks left
weeks_left_in_your_age = max_life_in_weeks - user_age_in_weeks

# Print the results on screen
print(f"You have {weeks_left_in_your_age} weeks left.")
