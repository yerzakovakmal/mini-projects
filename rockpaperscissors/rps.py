import random

u_name = str(input("What's Your Name?: "))

print("\t==== !!Welcome!! ==== " \
"\n ==== ROCK - PAPER - SCISSORS ====")
print("\t==== GAME LOGIC ====")
print("     -- Rock BEATS Scissors --")
print("     -- Scissors BEATS Paper --")
print("     -- Paper BEATS Rock --")
print("     -- SAME Choice = DRAW --")
print("!! 1 - Rock, 2 - Paper, 3 - Scissors !!")

while True:
    user_choice = int(input("Enter your choice (1-3): "))

    while user_choice > 3 or user_choice < 1:
        user_choice = int(input("Please enter a valid choice(1-3): "))

    if user_choice == 1:
        u_choice_val = "rock"
    elif user_choice == 2:
        u_choice_val = "paper"
    else:
        u_choice_val = "scissors"


    c_choice = random.randint(1, 3)

    if c_choice == 1:
        c_choice_val = "rock"
    elif c_choice == 2:
        c_choice_val = "paper"
    else:
        c_choice_val = "scissors"

    print("Computer choice:", c_choice_val)
    print("\n", u_choice_val, "VS", c_choice_val)


    if (user_choice == 2 and c_choice == 3) or (user_choice == 1 and c_choice == 2) or (user_choice == 3 and c_choice == 1):
        print("--> WINNER: Computer")
    elif (c_choice == 1 and user_choice == 2) or (c_choice == 2 and user_choice == 3) or (c_choice == 3 and user_choice == 1):
        print("--> WINNER:", u_name)
    else:
        print("--> DRAW")

    ans = input("Do you want to play again?(y/n): ").lower()
    if ans == 'n':
        break
print("\nThanks for playing!!")