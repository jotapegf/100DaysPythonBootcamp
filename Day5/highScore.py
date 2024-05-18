# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


high = student_scores[0]
for scores in student_scores:
  if scores > high:
    high = scores
print(f"The highest score in the class is: {high}")