import random

options = ["R", "P", "S"]
word = {"R": "Rock", "P": "Paper", "S": "Scissor"}

while True:
    user_input = input("Pick an option between 'R', 'P' or 'S'").upper()

    while user_input not in options:
        user_input = input("Please pick an option between 'R', 'P' or 'S' only.").upper()

    computer_choice = random.choice(options)

    print("Player", "(" + word[user_input] + ")", ":", "CPU", "(" + word[computer_choice] + ")")

    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "R" and computer_choice == "S") or (user_input == "S" and computer_choice == "P") or (user_input == "P" and computer_choice == "R"):
        print("User won!")
        break
    elif (user_input == "R" and computer_choice == "P") or (user_input == "S" and computer_choice == "R") or (user_input == "P" and computer_choice == "S"):
        print("Computer won!")
        break
