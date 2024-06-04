stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

import os
import random
os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
wordList = ["horse","apple","banana","python","book","smartphone","notebook","wallet","water","minecraft","university","house"]
display = []
gameOver = False

chosenWord = random.choice(wordList)

wordLength = len(chosenWord)

lives = 6
guessed = []

for letter in range(wordLength):
    display += "_"

while not gameOver:
    guess = input("Guess a letter: ").lower()
    
    os.system('cls' if os.name == 'nt' else 'clear')

    #if player already guessed the character
    if (guess in display):
        print(f"You've already guessed {guess}")


    for position in range(wordLength):
        letter = chosenWord[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosenWord:
        if(guess in guessed):
            print(f"You've already guessed {guess}")
        else:
            guessed += guess
            print(f'You guessed "{guess}", that\'s not in the word. You are closer to death.')
            lives -= 1
            print(f"You have {lives} attempts left.")
            if lives == 0:
                gameOver = True
                print("You lose!")
                print(f'The word was "{chosenWord}"!')
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        gameOver = True
        print("Congratulations! You Win!")
    
    print(stages[lives])
