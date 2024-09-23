# make a cash register

pennies = 0
nickels = 0
dimes = 0
quarters = 0
ones = 0
fives = 0
tens = 0
twenties = 0
fifties = 0
hundreds = 0


iPrice = float(input('Enter item price: '))
aPaid = float(input('Enter amount paid: '))
aOwed = 0
aDue = 0

#start

if aPaid < iPrice:
    aOwed = iPrice - aPaid
    aOwed = float(aOwed)
    print('You owe > ', aOwed)
else:
    aDue = float(aDue)
    print('Your change is > ', aDue)
    
