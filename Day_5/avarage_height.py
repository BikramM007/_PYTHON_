student_height = input("Input a list of students height:").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

print(student_height)

#total_height = sum(student_height)
total_height = 0
for height in student_height:
    total_height = total_height + height
print(total_height)

#no_of_student = len(student_height)
no_of_students = 0
for total in student_height:
    no_of_students = no_of_students + 1
print(no_of_students)

avarage_height = round(total_height / no_of_students)

print(avarage_height)