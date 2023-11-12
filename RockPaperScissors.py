from random import randint
from typing import *

options_lst = ["Rock", "Paper", "Scissors"]

def show_options(lst: List[str]) -> None:
    print("Welcome to the game of rock, paper, scissors!")
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
    if ia == user:
        return "Tie :/"
    elif (ia + 1) % len(options_lst) == user:
        return "Player wins :D"
    else:
        return "IA wins :("


ia, user = choices()

print(who_wins(ia, user))
