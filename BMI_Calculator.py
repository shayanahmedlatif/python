
# Ask height of a person
height = input(""" What is your height: """)

# Ask weight of a person
weight = input(""" What is your weight: """)

# Convert weight into integer
convert_weight = int(weight)
new_weight = convert_weight

# Now round the height input
convert_height = float(height)
new_height = convert_height

# Calculate BMI
bmi = (convert_weight / (new_height * new_height))

# Covert BMI into Whole number
new_bmi = int(bmi)

# Print New BMI
print(new_bmi)