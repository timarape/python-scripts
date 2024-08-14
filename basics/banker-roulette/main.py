import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

lastIndex = len(names)
picked = random.randint(0, (lastIndex- 1))

print(f"{names[picked]} is going to buy the meal today!")