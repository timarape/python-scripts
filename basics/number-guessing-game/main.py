import random
import math

lower = int(input("enter starting point integer\n"))
upper = int(input("Enter your end point "))

hiddenNumber = random.randint(lower, upper)
print("\n\tYou've only ",
	round(math.log(upper - lower + 1, 2)),
	" chances to guess the integer!\n")

count = 0
while count < math.log(upper - lower + 1, 2):
	count += 1
	
	guessedNumber = int(input("Guess a number "))
	if hiddenNumber == guessedNumber:
		print("Congratulations you did it in ",
			count, " try")
		break
	elif hiddenNumber > guessedNumber:
		print("You guessed too small, please try again")
	elif hiddenNumber < guessedNumber:
		print("You Guessed too high, please try again")

if count >= math.log(upper - lower + 1, 2):
	print("\nThe hiddedn number was %d" % hiddenNumber)



