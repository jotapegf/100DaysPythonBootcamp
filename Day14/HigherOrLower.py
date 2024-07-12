import art
from game_data import data
import random
import os


def formatData(account):    
    """Format the account data into printable format"""
    accountName = account["name"]
    accountDescr = account["description"]
    accountCountry = account["country"]
    return (f"{accountName}, a {accountDescr}, from {accountCountry}")

def checkAnswer(guess, followersA, followersB):
    """Take the user guess and follower counts and returns if they got it right"""
    if followersA > followersB:
        return guess == "a"
    else:
        return guess == "b"
    

score = 0
gameShouldContinue = True

accountB = random.choice(data)

while gameShouldContinue:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    accountA = accountB
    accountB = random.choice(data)
    if accountA == accountB:
        accountB = random.choice(data)

    print(f"Compare A: {formatData(accountA)}.")
    print(art.vs)
    print(f"Against B: {formatData(accountB)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    followerCountA = accountA["follower_count"]
    followerCountB = accountB["follower_count"]

    isCorrect = checkAnswer(guess, followerCountA, followerCountB)

    if isCorrect:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        gameShouldContinue = False
        print(f"Sorry, that's wrong. Final score: {score}")