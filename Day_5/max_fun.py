student_height = input("Input a list of students height:").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

for max in student_height:
    if student_height: