print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?



combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

score_true = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
score_love = l + o + v + e

final_score = int(str(score_true) + str(score_love))

if (final_score < 10 or final_score > 90):
  print(f"Your score is {final_score}, you go together like coke and mentos.")
elif(final_score > 40 and final_score < 50):
  print(f"Your score is {final_score}, you are alright together.")
else:
  print(f"Your score is {final_score}.")



