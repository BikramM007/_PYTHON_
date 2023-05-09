print("welcome to the rollercoaster")
height = int(input("what is your height in cm:"))

if height > 120:
    age = int(input("What is your age:"))

    if age < 12:
        bill = 5
        print("You have to pay $5")
    elif age <= 18:
        bill = 7
        print("you have to pay $7")
    elif age >=45 and age <=55:
        print("everything is going to be ok, Have your free ride")
    else:
        bill = 12
        print("You have to pay $5")

    want_photo = input("are you taken any photos? Y or N.")
    if want_photo == "Y":
        bill += 3


    print(f"Your final bill is {bill}")
else:
    print("you are not alligable for rollercoaster")