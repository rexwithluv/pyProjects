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


""" These functions are the ones that check that a player has won """
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


""" The check_choice() function uses the check_int_choice() and check_range_choice() functions to make the select_box() function more readable code. """
def check_choice(rc: str) -> int:
    def check_int(a: any, rc: str) -> int:
        while type(a) != int:
            try:
                a = int(a)
            except:
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
while play == True:
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