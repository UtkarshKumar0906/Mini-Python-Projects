import random

number = random.randrange(20)
tries = 0

while True:
    tries += 1

    guess = input("Try to guess between 0 to 20 \n")
    number = int(number)

    if guess.isdigit():
        guess = int(guess)

    if guess == number:
        print("Yes! The number is infact", number)
        break
    elif guess > number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in ", tries, "tries" )