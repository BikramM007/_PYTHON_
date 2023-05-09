original_list = [1,2,3,4,5,6,7,8,9]
reversed_list = list()

for item in original_list:
    reversed_list = [item] + reversed_list

print(reversed_list)