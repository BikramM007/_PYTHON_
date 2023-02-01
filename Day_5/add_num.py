number2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        number2 += number
print(number2)

number2 = 0
for number in range(2, 101, 2):
    number2 += number
print(number2)