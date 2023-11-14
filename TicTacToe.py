from typing import Union, List, Tuple


def players_names() -> Tuple[str, str]:
    player1 = input("Name of player 1: ")
    player2 = input("Name of player 2: ")

    if player1 == "":
        player1 = "Player 1"

    if player2 == "":
        player2 = "Player 2"

    return player1, player2


def show_table(lst: List[str]) -> None:
    for i in lst:
        print("        ", end="")
        for j in i:
            print(j, end=" ")
        print()


def win(lst: List[str]) -> Union[None, str]:
    def row_win(lst: List[str]) -> Union[None, str]:
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

    def column_win(lst: List[str]) -> Union[None, str]:
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

    def diagonally_win(lst: List[str]) -> Union[None, str]:
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

    row_win(lst)
    column_win(lst)
    diagonally_win(lst)

    if isinstance(row_win(table), str):
        return row_win(table)
    elif isinstance(column_win(table), str):
        return column_win(table)
    elif isinstance(diagonally_win(table), str):
        return diagonally_win(table)


def check_choice(rc: str) -> int:
    def check_int(a: any, rc: str) -> int:
        while type(a) != int:
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

    a = input(f"Give me the {rc} (1, 2, 3): ")

    a = check_int(a, rc)
    a = check_range(a, rc)

    return a


def select_box(table: List[List[str]]) -> None:
    row = check_choice("row")
    column = check_choice("column")

    while table[row - 1][column - 1] != "_":
        print("This box is occupied. Select another one.")
        row = check_choice("row")
        column = check_choice("column")
    else:
        table[row - 1][column - 1] = symbol

    show_table(table)


play = True
while play:
    print("Welcome to TicTacToe game!")
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

    again = input("Do you want to play again? (y/n) ").lower()
    if again == "yes" or again == "y":
        play = True
    elif again == "no" or again == "n":
        print("I hope you enjoyed the game. See you soon!")
        play = False
