
def questions():

    play = input("Do you want to start the game (y/n): ").lower()
    if play != "y":
        quit()

    score = 0
    answer = input("What is the capital of France? ").lower()
    if answer == "paris":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is Paris.\n")

    answer = input("In which year did World War II end? ").lower()
    if answer == "1945":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is 1945.\n")

    answer = input("Which planet is known as the 'Red Planet'? ").lower()
    if answer == "mars":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is Mars.\n")

    answer = input("Who wrote the play 'Romeo and Juliet'? ").lower()
    if answer == "william shakespeare":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is William Shakespeare.\n")

    answer = input("What is the largest mammal in the world? ").lower()
    if answer == "blue whale":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is Blue Whale.\n")

    answer = input("Which programming language is often used for web development? ").lower()
    if answer == "html" or answer == "js":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is HTML.\n")

    answer = input("Who is known as the 'Father of Computer Science'? ").lower()
    if answer == "alan turing":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is Alan Turing.\n")

    answer = input("What is the chemical symbol for gold? ").lower()
    if answer == "au":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is Au.\n")

    answer = input("Which ocean is the largest on Earth? ").lower()
    if answer == "pacific ocean" or answer =="pacific":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is Pacific Ocean.\n")

    answer = input("How many continents are there in the world? ").lower()
    if answer == "7":
        print("Correct!\n")
        score +=1
    else:
        print("Incorrect. The correct answer is 7.\n")

    print("You got " + str(score) + " questions correct!")
    print("You got " + str(score * 10) + "%.") # score/10 * 100 would be score *10

questions()