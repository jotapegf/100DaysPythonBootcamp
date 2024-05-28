
def prime_checker(number):
  answer = 0
  for i in range(1, number + 1):
    if (number % i == 0):
      answer += 1
  if answer <= 2:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


n = int(input()) # Check this number
prime_checker(number=n)