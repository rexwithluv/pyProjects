from typing import Union, List, Tuple


def players_names() -> Tuple[str, str]:
    user1 = input("Name of player 1: ")
    user2 = input("Name of player 2: ")

    if user1 == "":
        user1 = "Player 1"

    if user2 == "":
        user2 = "Player 2"

    return user1, user2


def show_table(lst: List[str]) -> None:
    for i in lst:
        print("        ", end="")
        for j in i:
            print(j, end=" ")
        print()


def win_row(lst: List[str]) -> Union[None, str]:
    for count, i in enumerate(lst):
        if count == 0:
            position = "top"
        elif count == 1:
            position = "middle"
        else:
            position = "bottom"

        if i[0] == "x" and i[1] == "x" and i[2] == "x":
            return f"{player1} has won in the {position} row."
        elif i[0] == "o" and i[1] == "o" and i[2] == "o":
            return f"{player2} has won in the {position} row."


def win_column(lst: List[str]) -> Union[None, str]:
    # This block transposes the list
    transpose = []
    for i in range(3):
        add_to_transpose = []
        for j in lst:
            add_to_transpose.append(j[i])
        transpose.append(add_to_transpose)

    # Here we check if you have won, who and in which column.
    for count, i in enumerate(transpose):
        if count == 0:
            position = "left"
        elif count == 1:
            position = "middle"
        else:
            position = "right"

        if i[0] == "x" and i[1] == "x" and i[2] == "x":
            return f"{player1} has won in the {position} column."
        elif i[0] == "o" and i[1] == "o" and i[2] == "o":
            return f"{player2} has won in the {position} column."


def win_diagonally(lst: List[str]) -> Union[None, str]:
    # With this we find out the descending diagonal
    diagonal = []
    for count, i in enumerate(lst):
        diagonal.append(i[count])

    if diagonal[0] == "x" and diagonal[1] == "x" and diagonal[2] == "x":
        return f"{player1} has won in the downward diagonal."
    elif diagonal[0] == "o" and diagonal[1] == "o" and diagonal[2] == "o":
        return f"{player2} has won in the downward diagonal."

    # With this we find out the ascending diagonal
    diagonal = []
    for count, i in enumerate(reversed(lst)):
        diagonal.append(i[count])

    if diagonal[0] == "x" and diagonal[1] == "x" and diagonal[2] == "x":
        return f"{player1} has won in the upward diagonal."
    elif diagonal[0] == "o" and diagonal[1] == "o" and diagonal[2] == "o":
        return f"{player2} has won in the upward diagonal."


def win(table: List[str]) -> Union[None, str]:
    if isinstance(win_row(table), str):
        return win_row(table)
    elif isinstance(win_column(table), str):
        return win_column(table)
    elif isinstance(win_diagonally(table), str):
        return win_diagonally(table)


def check_int(a: any, rc: str) -> int:
    while type(a) is not int:
        try:
            a = int(a)
        except ValueError:
            print("This option is not a number. Please select another one.")
            a = input(f"Give me the {rc} (1, 2, 3): ")

    return a


def check_range(a: any, rc: str) -> int:
    while a not in range(1, 4):
        print("This option is not in range. Please select another one.")
        a = input(f"Give me the {rc} (1, 2, 3): ")
        a = check_int(a, rc)

    return a


def check(rc: str) -> int:
    a = input(f"Give me the {rc} (1, 2, 3): ")

    a = check_int(a, rc)
    a = check_range(a, rc)

    return a


def select_box(tbl: List[List[str]]) -> None:
    row = check("row")
    column = check("column")

    while tbl[row - 1][column - 1] != "_":
        print("This box is occupied. Select another one.")
        row = check("row")
        column = check("column")
    else:
        tbl[row - 1][column - 1] = symbol

    show_table(tbl)


def play_again():
    again = input("Do you want to play again? (y/n) ").lower()
    if again == "yes" or again == "y":
        return True
    elif again == "no" or again == "n":
        print("I hope you enjoyed the game. See you soon!")
        return False


print("Welcome to TicTacToe game!")
play = True
while play:
    player1, player2 = players_names()

    table = [["_" for j in range(3)] for i in range(3)]
    show_table(table)

    for i in range(9):
        if i % 2 == 0:
            print(f"It's your turn {player1}")
            symbol = "x"
        else:
            print(f"It's your turn {player2}")
            symbol = "o"

        select_box(table)

        if isinstance(win(table), str):
            print(win(table))
            break

    play = play_again()
