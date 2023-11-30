# This program will select the random name from the list
# And print out the message on the screen
# For this to work, we'll use random buitin random funciton
import random

# Names list
names = ["Liam", "Noah", "Oliver", "Harry", "Jacob", "Leo", "Charlie", "Amelia", "Isla", "Ava"]

# Now, we'll use the random funtion to get the random 
# Number of a specific name
# This line of code below will convert the specific name
# Into a excat number by using the len() function.

generat_random_name = random.randrange(len(names))


# Now, we got the index number of the names var
# by using this random index number, we'll generate 
# Random name via print command

rand_name = names[generat_random_name]

# Print the rand name into the screen.

# print(f"{rand_name}, will pay the bill today.")
# print(len(names))
print(rand_name)