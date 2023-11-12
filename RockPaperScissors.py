from random import randint
from typing import *

options_lst = ["Rock", "Paper", "Scissors"]

def show_options(lst: List[str]) -> None:
    for count, i in enumerate(options_lst):
        print(f"  {count + 1}.- {i}")

def choices() -> Tuple[int]:
    ia = randint(0, 2)

    show_options(options_lst)
    user = input("Which one do you choose? (1, 2, 3) ")

    while type(user) != int:
        try:
            user = int(user)
        except:
            print("This option is not valid. Please select another one.")
            user = input("Which one do you choose? (1, 2, 3) ")

    while user not in range(1, 4):
        print("This option is not valid. Please select another one.")
        user = int(input("Which one do you choose? "))
    

    return ia, user
        
def who_wins(ia: int, user: int) -> str:
    user -= 1
    if ia == user:
        return "Tie :/"
    elif (ia + 1) % len(options_lst) == user:
        return "Player wins :D"
    else:
        return "IA wins :("

def play_again() -> bool:
    while True:
        again = input("Do you want to play again? (y/n) ").lower()
        if again == "yes" or again == "y":
            return True
        elif again == "no" or again == "n":
            print("I hope you enjoyed the game. See you soon!")
            return False
        else:
            print("This option is not valid.")


print("Welcome to the game of rock, paper, scissors!")
play = True
while play:
    ia, user = choices()
    print(f"IA chose {options_lst[ia]}")
    print(who_wins(ia, user))

    play = play_again()
