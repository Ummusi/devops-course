
'''''
*** biggest number in list

numbers = [5, 6, 7, 8, 12, 3, 21]
biggest_number = numbers[0]
for number in numbers:
    if number > biggest_number:
        biggest_number = number
print(biggest_number)


*** F letter
stars=(6,2,6,2,2)
for star in stars:
    letter = ''
    for value in range(star):
        letter += 'x'
    print(letter)


*** program to start a car with command, and if it is started, warnings about that.

status = 'begin'
while True:
    command= input("> ").lower()
    if command == status:
        print(f'car is already {status}ed')
    else:
        if command == 'start':
            status = 'start'
            print("Car Started")
        elif command == 'stop':
            print("Car Stopped")
            status = 'stop'
        elif command == 'help':
            print("""  
Press Start to start the car...
Pres Stop to stop it, 
and quit to exit""")
        else:
            break


*** Guess number

guess_number = 9
num_tries=0
try_limit =3

while num_tries < try_limit:
    number = int(input("Guess the number: "))
    num_tries += 1
    if number == guess_number:
        print ("you won")
        break
else:
    print("\n Sorry, you ran out of guesses!")

-- Second method:


guess_number = 9
out_of_guesses = False
guess_try = 0
number = ''

while not out_of_guesses and number != guess_number:
    number = int(input("Guess the number: "))
    if number == guess_number:
        print("You won!")
    else:
        guess_try += 1
        if guess_try == 3:
            out_of_guesses = True
            print("You ran out of guesses!")


*** kilogram to pound converter
-----
weight = input ("Your weight: ")
unit = input("Is it Kilogram or Pound? \n Press K for Kilogram  or P for Pound: ")

if unit.lower()== "k":
    weight=float(weight) * 2.204
    print (f'You are {round(weight,2)} pound')
else:
    weight = float(weight) / 2.204
    print(f'You are {round(weight,2)} Kg')
-----
*** prints sale of a house if buyer has good credit or not
---
house_price = 1000000
good_credit = False
if good_credit:
    sale = house_price * 0.1
else:
    sale = house_price * 0.2
print(f"Sale is: ${sale}")

'''
