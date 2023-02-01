print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1 + name2
lower_case_string = combine_name.lower()

T = lower_case_string.count("t")
R = lower_case_string.count("r")
U = lower_case_string.count("u")
E = lower_case_string.count("e")

TRUE = T + R + U + E

L = lower_case_string.count("l")
O = lower_case_string.count("o")
V = lower_case_string.count("v")
E = lower_case_string.count("e")

LOVE = L + O + V + E

love_score = int(str(TRUE) + str(LOVE))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")          
elif (love_score >= 40) or (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")