#calculator making 

#add 
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#multiply
def multiply(n1, n2):
    return n1 * n2

#devided
def devision(n1, n2):
    return n1 / n2

operation = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":devision
}

num1 = int(input("what is first number:"))
num2 = int(input("What is second number:"))

for symbol in operation:
    print(symbol)

operation_symbol = input("Pick the operation from the line above:")

operation_function = operation[operation_symbol]
answer = operation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
