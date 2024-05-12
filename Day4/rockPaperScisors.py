import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [rock, paper, scissors]

print("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.")

userChoice = int(input())
choices = [0, 1, 2]
if userChoice >= 3 or userChoice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(gameImages[userChoice])

computersChoice = random.randint(0, 2)
print(f"Computer chose: {computersChoice}")
print(gameImages[computersChoice])


if(userChoice == 0 and computersChoice == 2):
    print("You win!")
elif computersChoice == 0 and userChoice == 2:
    print("You lose")
elif computersChoice > userChoice:
    print("You lose!")
elif userChoice > computersChoice:
    print("You win!")
elif(userChoice == computersChoice):
    print("It's a draw")




