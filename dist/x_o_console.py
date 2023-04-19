#!/usr/bin/python3
"""This file is a simple fun console X and 0 game
for anyone interested in this age long sport. The game is
built kind of bogus cos there's no list inside it :) Only
loops, strings and conditionals
"""

def print_string(game, score, index):
    """This prints out the game at every turn. It accepts parameters
    of score and index to enable it print out the lines when they match
    Args: game->  The game string
          score-> The currrent score it's 0 if ther's no score
                  and non 0 if there's a score
          index-> The index where the score is. It is None if there's
                  no index
    Return: Nothing as it is a print function
    """
    print("    0       1      2  ")
    print(" +--------------------+")
    x = 0
    for i in range(3):
        var1 = " |      |      |      |"
        res = "{}|   {}  |   {}  |   {}  |".format(i, game[0 + x], game[1 + x], game[2 + x])
        if score == 2:
            if index == 0:
                var1 = " |   |  |      |      |"
            elif index == 1:
                var1 = " |      |   |  |      |"
            elif index == 2:
                var1 = " |      |      |   |  |" 
        var2 = var1
        if index == 0 + x and score == 1:
            res = "{}|---{}--|---{}--|---{}--|".format(i, game[0 + x], game[1 + x], game[2 + x])
        if score == 3:
            if 0 + x == 0:
                var1 = " |*     |      |      |"
                var2 = " |     *|      |      |"
            if 1 + x == 4:
                var1 = " |      |*     |      |"
                var2 = " |      |     *|      |"
            if 2 + x == 8:
                var1 = " |      |      |*     |"
                var2 = " |      |      |     *|"
        if score == 4:
            if 2 + x == 2:
                var1 = " |      |      |     *|"
                var2 = " |      |      |*     |"
            if 1 + x == 4:
                var1 = " |      |     *|      |"
                var2 = " |      |*     |      |"
            if 0 + x == 6:
                var1 = " |     *|      |      |"
                var2 = " |*     |      |      |"
        print(var1)
        print(res)
        print(var2)
        print(" +--------------------+")
        x += 3

def check(game, i):
    """This function checks the edges to know if a score has been made
    Args: game-> the game string
          i-> the index being checked
    Return 1-> Vertical match
           2-> Vertical match
           3-> Leading diagonal match
           4-> Second diagonal match
           0-> No match
    """
    if game[i] != " ":
        if ((i == 0 or i == 3 or i == 6) and 
                game[i] == game[i + 1] == game[i + 2]):
            return 1
        if ((i == 0 or i == 1 or i == 2) and
                game[i] == game[i + 3] == game[i + 6]):
            return 2
        if (i == 0) and game[0] == game[4] == game[8]:
            return 3
        if (i == 2) and game[2] == game[4] == game[6]:
            return 4
    return 0

def check_score(game):
    """This calls the check function to check the corner
    points. It then prints out the string as the X & 0 boxes
    Args: game-> The game string
    Return: True if there's a match, false if there isn't
    """
    pos="01236"
    mark = 0
    index = None
    for i in range(5):
        mark = check(game, int(pos[i]))
        if mark > 0:
            index = int(pos[i])
            break
    print_string(game, mark, index)
    if mark > 0:
        return True
    return False


def prompt(player):
    """This prompts the players for their coordinates. it handles
    errors like letters and wrong coordinates or where a space is
    already occupied
    Args: player-> The current players turn
    Return: The position of his figure
    """
    value = input(f"Enter your position player {player}: ")
    if value == "q" or value.lower() == "quit":
        return -1
    while ((len(value) != 2) or (len(value) == 2 and ((value[0] not in "0123") or
            (value[1] not in "0123")))):
        value = input(f"Please player {player} enter in a valid coordinate: ")
        if value == "q" or value.lower() == "quit":
            return -1
    pos = 3 * int(value[0]) + int(value[-1])
    return pos

def run_game(game):
    """This is our driver function to run the game
    It makes use of the other utility functions in
    a loop
    Args: game-> The initial game string
    """
    flag = True
    print_string(game, 0, None)
    man = "X"
    for i in range(1,10):
        rem = man
        pos = prompt(man)
        while game[pos] != ' ':
            print(f"I'm so sorry, {game[pos]} is already here")
            pos = prompt(man) 
        if pos == -1:
            print("\n----------C-A-N-C-E-L-L-E-D-----------\n")
            return -1
        if flag == True:
            game = game[:pos] + "X" + game[pos + 1:]
            man = "0"
            flag = False
        elif flag == False:
            game = game[:pos] + "O" + game[pos + 1:]
            man = "X"
            flag = True
        curr = check_score(game)
        if curr:
            print(f"\n------P-L-A-Y-E-R {rem} W-I-N-S-------\n")
            return
    
    print(f"\n-----------------D-R-A-W-----------\n")
if __name__ == "__main__":
    game = "         "
    print("Welcome to our mini Xs and Os. This is just a fun project and should be taken")
    print("with a grain of salt. The rules are very simple: ")
    print("1-> Players enter coordinates in the form RC where R is row and C is column")
    print("2-> To quit, type q or press quit. The game is automatically unfinished")
    print("3-> There's no 'replay' :) so think carefully before you play")
    print("4-> Good luck")
    while True:
        mark = run_game(game)
        print("---D-O--Y-O-U--W-A-N-T--T-O--C-O-N-T-I-N-U-E--P-L-A-Y-I-N-G---")
        mask = input("Y/N: ")
        if mask == "Y":
            mark = -1
        elif mask == "N":
            mark = run_gamr(game)
        else:
            print("Defaulting to yes")
            continue
        if mark == -1:
            print("\n-----T-H-A-N-K-S---F-O-R---P-L-A-Y-I-N-G------\n")
            break
