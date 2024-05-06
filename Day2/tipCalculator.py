print("Welcome to the bill calculator!\n")

bill = float(input("What was the total bill? $"))
tip_percentage = float(input("How much will be the percentage of the tip? 10, 20, 5... "))
people = int(input("How many people will split the bill?"))

total_per_person = (bill + (bill * (tip_percentage / 100))) / people

total_per_person = "{:.2f}".format(total_per_person)
print(f"\nEach person should pay: ${total_per_person}")