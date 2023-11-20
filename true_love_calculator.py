# This program will calculate the score between two peoples names
name1 = "Shayan"
name2 = "Rabia"

name1 = name1.lower()
name2 = name2.lower()

# Count the TRUE & LOVE in name1
N1T = name1.count("t")
N1R = name1.count("r")
N1U = name1.count("u")
N1E1 = name1.count("e")

N1L = name1.count("l")
N1O = name1.count("o")
N1V = name1.count("v")
N1E2 = name1.count("e")

# Count the TRUE & LOVE in name2
N2T = name2.count("t")
N2R = name2.count("r")
N2U = name2.count("u")
N2E1 = name2.count("e")

N2L = name2.count("l")
N2O = name2.count("o")
N2V = name2.count("v")
N2E2 = name2.count("e")

name12_true = N1T + N1R + N1U + N1E1 + N2T + N2R + N2U + N2E1
name12_love = N1L + N1O + N1V + N1E2 + N2L + N2O + N2V + N2E2

love_score = int(f"{name12_true}{name12_love}")

if love_score < 10:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
