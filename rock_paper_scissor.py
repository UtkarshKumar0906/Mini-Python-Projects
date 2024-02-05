import random
print("Welcome to Rock, Paper and Scissors!!!")
print("First to five points win")

user_score = 0
computer_score = 0

options = ["rock","paper","scissors"]

while True:
    user = input("Rock /Paper /Scissors or q to quit: ").lower()
    random_number = random.randint(0,2)
    computer = options[random_number]

    if user == 'q':
        break

    if user not in options:
        print("Not a valid option")
        continue

    print("Computer picked", computer + ".")

    if user == 'rock' and computer == 'scissors':
        print("You win!")
        user_score += 1
    elif user == 'paper' and computer == 'rock':
        print("You Win!")
        user_score += 1
    elif user == 'scissors' and computer == 'paper':
        print("You Win!")
        user_score += 1
    elif user == computer:
        print("A Draw")
    else:
        print("Computer wins")
        computer_score += 1
    
    if user_score == 5 or computer_score == 5:
        break

print ("Bye Bye!")