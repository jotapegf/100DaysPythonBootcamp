import os
os.system('cls' if os.name == 'nt' else 'clear')
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

def caesar(startText, shiftAmount, cipherDirection):
    endText = ""
    if cipherDirection == "decode":
            shiftAmount *= -1
    for char in startText:
        if char in alphabet: 
            position = alphabet.index(char)
            newPosition = position + shiftAmount
            endText += alphabet[newPosition]
        else:
             endText += char
    print(f"The {cipherDirection}d text is {endText}")

shouldContinue = True
while shouldContinue:
    choice = input('Type "encode" to encrypt, type "decode" to decrypt: \n')
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    shift = shift % 26
    caesar(startText=text, shiftAmount=shift, cipherDirection=choice)
    instruction = input('Type "yes" if you want to go again. Otherwise, type "no".\n')
    if instruction == "no":
         shouldContinue = False
         print("Goodbye!")