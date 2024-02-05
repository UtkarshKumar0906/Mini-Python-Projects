import time
def make_choice(options):
    print("Choose your option: ")
    for i, option in enumerate(options,1):
        print(f"{i}.{option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
def introduction():
    print("Welcome to the Clover Kingdom!!!")
    time.sleep(1)
    Name = input("What is your name: ")
    time.sleep(1)
    print("In the outskirts of the Clover Kingdom, you are," ,Name, " an aspiring mage with a unique magical affinity for shadows. Your journey begins when you discover an ancient artifact that unveils a hidden power within you.")
    
def Chapter1():
    print("\nWelcome to chapter one!!")
    time.sleep(1)
    print("The ancient artifact grants you mysterious shadow-based abilities.")
    time.sleep(1)
    print("Now, you must decide how to harness and develop this newfound power:")

    choices = ["Embrace the shadows",
                "Explore defensive applications",
                "Seek mystical guidance"]
    
    choice = make_choice(choices)

    if choice == 1:
        print("Focus on offensive capabilities, honing your skills for powerful attacks.")
    elif choice == 2:
        print("Develop protective spells to shield yourself and others from harm.")
    else:
        print(" Consult ancient texts or wise mystics to understand the origin and potential of your powers.")



introduction()
Chapter1()