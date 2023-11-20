char_list = ['S', 'h', 'a', 'y', 'a', 'n']

# Using a loop to create variables dynamically
for index, char in enumerate(char_list):
    var_name = f"char_{index + 1}"
    globals()[var_name] = char

# # Now, you have variables char_1, char_2, ..., char_6 containing each character
# print(char_1)  # Output: S
# print(char_2)  # Output: h
# # ... and so on

# To print each char value
for index in range(1, len(char_list) + 1):
    print(globals()[f"char_{index}"])
