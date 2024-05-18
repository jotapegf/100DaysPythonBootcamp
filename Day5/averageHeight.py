# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


totalHeight = 0
for height in student_heights:
  totalHeight += height
print(f"total height = {totalHeight}")

studentsNumber = 0
for student in student_heights:
  studentsNumber += 1
print(f"number of students = {studentsNumber}")

average = totalHeight / studentsNumber
print(f"average height = {round(average)}")

