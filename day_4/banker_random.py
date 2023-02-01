import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_len = len(names)

random_no = random.randint(0 , names_len-1)

random_rs = names[random_no]

print(f"{random_rs} is going to buy the meal today!")
