import random

user_wins = 0
computer_wins = 0

options = ["r", "p", "s"]

while True:
    user = input("Type r for Rock, p for Paperr, s for Scissors or q to quit: ").lower()
    if user == "q":
        break

    if user not in options:
        continue

    random_pick = random.randint(0, 2)
    # r: 0, p: 1, s: 2
    computer_choice = options[random_pick]
    print(" The Computer picked", computer_choice + ".")

    if user == "r" and computer_choice == "s":
        print("You won!")
        user_wins += 1

    elif user == "p" and computer_choice == "r":
        print("You won!")
        user_wins += 1

    elif user == "s" and computer_choice == "p":
        print("You won!")
        user_wins += 1

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Thank You for playing!")