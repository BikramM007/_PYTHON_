# filename = "/home/bikram007/Desktop/python_007/sir/file.txt"  

# with open(filename, 'r') as file:
#     lines = file.readlines()

# for line in reversed(lines):
#     print(line.strip())



import os
import time

filename = "/home/bikram007/Desktop/python_007/sir/file.txt"  

with open(filename, 'w') as file:
    file.write("Cows are domesticated mammals that are commonly raised for their meat, milk, and hides.")

with open(filename, 'r') as file:
    content = file.read()
print(content)

time.sleep(2)


reversed_content = content[::-1]

with open(filename, 'w') as file:
    file.write(reversed_content)

print(reversed_content)

time.sleep(2)
spaces = 





