from typing import Union, List, Tuple


def show_table(lst: List[str]) -> None:
    for i in lst:
        for j in i:
            print(j, end=" ")
        print()

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
    # Con esto transponemos la lista
    transpose = []
    for i in range(3):
        add_to_transpose = []
        for j in lst:
            add_to_transpose.append(j[i])
        transpose.append(add_to_transpose)
        

    # Aquí comprobamos que si ha ganado, quién y en que columna
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
    # Con esto averiguamos la diagonal descendente
    diagonal = []
    for count, i in enumerate(lst):
        diagonal.append(i[count])
    
    if diagonal[0] == "x" and diagonal[1] == "x" and diagonal[2] == "x":
        return f"{player1} has won in the downward diagonal."
    elif diagonal[0] == "o" and diagonal[1] == "o" and diagonal[2] == "o":
        return f"{player2} has won in the downward diagonal."

    # Con esto averiguamos la diagonal ascendente
    diagonal = []
    for count, i in enumerate(reversed(lst)):
        diagonal.append(i[count])

    if diagonal[0] == "x" and diagonal[1] == "x" and diagonal[2] == "x":
        return f"{player1} has won in the upward diagonal."
    elif diagonal[0] == "o" and diagonal[1] == "o" and diagonal[2] == "o":
        return f"{player2} has won in the upward diagonal."

def players_names() -> Tuple[str, str]:
    player1 = input("Name of player 1: ")
    player2 = input("Name of player 2: ")

    if player1 == "":
        player1 = "Player 1"
    
    if player2 == "":
        player2 = "Player 2"
    
    return player1, player2

def select_box(table: List[List[str]]) -> None:
    row = int(input("Give me the row (1, 2, 3): "))
    column = int(input("Give me the column (1, 2, 3): "))

    while table[row - 1][column - 1] != "_":
        print("This box is occupied. Select another one.")
        row= int(input("Give me the row (1, 2, 3): "))
        column = int(input("Give me the column (1, 2, 3): "))
    else:
        table[row - 1][column - 1] = symbol



player1, player2 = players_names()


play = True
while play == True:
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

        show_table(table)

        if isinstance(row_win(table), str):
            print(row_win(table))
            break
        elif isinstance(column_win(table), str):
            print(column_win(table))
            break
        elif isinstance(diagonally_win(table), str):
            print(diagonally_win(table))
            break

    
    again = input("Do you want to play again? (y/n) ").lower()
    if again == "yes" or again == "y":
        play = True
    elif again == "no" or again == "n":
        print("I hope you enjoyed the game. See you soon!")
        play = False