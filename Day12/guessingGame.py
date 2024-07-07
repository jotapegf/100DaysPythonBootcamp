import random
import os

isGameOver = False


def setDifficulty():
    difficulty = 'none'
    while difficulty != 'hard' and difficulty != 'easy':
        difficulty = input("Choose the game difficulty. Type 'hard' or 'easy': ")
        if difficulty == 'hard':
            return 5
        elif difficulty == 'easy':
            return 10

def compare(guess, secretNumber):
    global isGameOver
    if guess > secretNumber:
        print("Too high.")
        return -1
    elif guess < secretNumber:
        print("Too low.")
        return -1
    else:
        isGameOver = True
        return 0

def playGame():
    global isGameOver
    print("Welcome to the guessing Game!")

    while not isGameOver:
        attempts = setDifficulty()
        print(f"You have {attempts} attempts!")

        secretNumber = random.randint(0, 100)
        while attempts > 0:    
            guess = int(input("Guess a number between 0 and 100: "))

            attempts += compare(guess, secretNumber)

            if attempts < 1:
                print("You have no more attempts! You lose!")
                isGameOver = True
            elif isGameOver == True:
                attempts = 0
                print("You win!")

    while input("Do you want to play again? 'y' or 'n'") == 'y':
        os.system('cls' if os.name == 'nt' else 'clear')
        isGameOver = False
        playGame()

        
playGame()



    