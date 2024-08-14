splitAmount = 0.0
paymentPerPerson = 0.0

print("Welcome to the tip calculator")
totalBill = float(input(print("What was the total bill?")))
numberOfPeople = int(input(print("How many people to split the bill?")))
tipPercentage = int(input(print("What persantage tip would you like to give? 10, 12 or 15")))

splitAmount = totalBill/numberOfPeople
if(tipPercentage == 10):
    paymentPerPerson = splitAmount + (0.10*splitAmount)
elif(tipPercentage == 12):
    paymentPerPerson = splitAmount + (0.12*splitAmount)

elif(tipPercentage == 15):
    paymentPerPerson = splitAmount + (0.15*splitAmount)

print("Each person will pay: "+str(paymentPerPerson))