target = int(input()) # Enter a number between 0 and 1000

evenSum = 0
for i in range (0, target+1, 2):
  evenSum += i
print(evenSum)