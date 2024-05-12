import random

# Recebendo os nomes como entrada
names_string = input("Digite os nomes separados por vírgula e espaço: ")
names = names_string.split(", ")


numItens = len(names)
selectedNumber = random.randint(0, numItens-1)
print(f"{names[selectedNumber]} is going to buy the meal today!")
