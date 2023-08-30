from sys import argv, exit
from random import choice
from tabulate import tabulate


class Table:
    """
    table is the x/o columns and rows
    :Table print returns a string (table with values)

    ATTRIBUTES:
    :type self.table dict
    :self.table dict excpects 'x', 'o', None if empty
    self.x contains all the notations occupied by x
    self.o contains all the notations occupied by o
    self.available contains all the free notations

    INIT METHOD:
    initializes the table to empty table

    STRING METHOD:
    returns the table with all data in the right format using tabulate

    METHODS:
    generate_table() generates table with empty columns and row [a1 - c3]
    generate_possibilities() generates all possible solutions to tic tac toe

    add(notation, char) adds char to the provided notation,
    if Notation is already occupied it raises a ValueError
    if Notation doesn't exist it raises a TypeError

    check() checks wether the game ended or no
    the game end of win if one player get's a straigt/diognal line (3 blocks)
    the game ties of all blockes get full and no one gets a straight or diognal line (3 blocks)
    check return "x" or "o" if a user wins "tie" if all places gets full and None if the game is still going
    """

    def __init__(self):
        self.table = self.generate_table()
        self.possibilities = self.generate_possibilities()
        self.x = []
        self.o = []
        self.available = [notation for notation in self.table]

    def __str__(self):
        table = self.table
        formated_table = {
            "nt": [1, 2, 3],
        }

        # loop into each column in table
        for column in table:
            letter, number = column
            # if letter is not in the dict add a new list
            if letter not in formated_table:
               formated_table[letter] = []

            # append value to the list
            formated_table[letter].append(table[column])

        # return table in the right format
        return tabulate(formated_table, headers=["nt", "a", "b", "c"], tablefmt="grid")

    def generate_table(self):
        game_dict = {}
        for column in ["a", "b", "c"]:
            for row in ["1", "2", "3"]:
                game_dict[column + row] = None
        return game_dict

    def generate_possibilities(self):
        # possibilites: at least three notations have :
        # 1. letters are in order and number is the same
        # 2. letters are the same and numbers are in order
        # 3. letters are in order and numbers are order (ascending or descending)
        possibilities = [["a1", "b2", "c3"], ["a3", "b2", "c1"]]
        columns = ["a", "b", "c"]
        rows = ["1", "2", "3"]

        # generate all possible rows
        for column in columns:
            notations = []
            for row in rows:
                notations.append(column + row)
            possibilities.append(notations)

        # generate all possible columns
        for row in rows:
            notations = []
            for column in columns:
                notations.append(column + row)
            possibilities.append(notations)

        return possibilities

    def add(self, notation, char):
        table = self.table
        char = char.lower()
        notation = notation.lower()

        # if notation is valid and it is not occupied
        # assign char to notation
        if notation in table and table[notation] == None and char in ["x", "o"]:
            table[notation] = char
            if char == "x":
                self.x.append(notation)
            else:
                self.o.append(notation)

            self.available.remove(notation)

            # return game state (win("x", "o"), tie("tie"), game didn't end(None))
            return self.check()

        # elif notation doesn't exist raise a TypeError
        elif notation not in table:
            raise ValueError(f"Notation ({notation}) provided doesn't exist")
        # elif notation is occupied raise a ValueError
        elif table[notation] != None:
            raise ValueError(f"Notation is occupied")
        # raise type error becuase char isnt x or o
        else:
            raise TypeError(f"Char should be either (x, o) not ({char})")

    def check(self):
        possibilities = self.possibilities
        players = {"x":self.x, "o":self.o}

        # check for win
        for player in players:
            notations = sorted(players[player])
            if notations in possibilities:
                return player

        # check for tie
        if self.available == []:
            return "tie"

        # if no condition is met then the game didnt end
        return None

# scores
x = 0
o = 0

def main():
    """
    main function contains three main variables:
    global x which contains the score of x player
    global o which contains the score of o player
    players which calls the get_players() function to get the number of players whom are playing

    IMPLEMENTATION:
    there is a forever loop where:
    it first calls the simulate_game function passing players number to get the winner of the game
    it increments the winner 's score by one, if it is tie then both will be incremented by one
    the function will print the scores of both user
    and finally ask for a remetech: y: accepted, n: quite program other: re-ask
    """
    # variables
    global x
    global o
    players = get_players()

    while True:
        # start game
        winner = simulate_game(players)

        # add scores
        if winner == "x":
            x += 1
        elif winner == "o":
            o += 1
        else:
            x += 1
            o += 1

        # print scores
        print(f"x:{x} - o:{o}")

        # ask for a re-match
        while True:
            awnser = input("Do you want a re-match(y\\n): ")
            char_awnser = awnser[0].lower()
            if char_awnser == "y":
                break
            elif char_awnser == "n":
                exit(0)

def get_players():
    """
    Get player function returns an int (1 or 2)
    it returns number of players whom are going to play

    it checks the user input if he inputed 1 or 2 it will be returned
    if he didn't input anything 2 will be returned
    if he inputs anyother thing the system will quit and show usage to user
    """
    invalid_input_error = "Usage: python tic-tac-toe.py {players_count}(1 or 2)"
    if len(argv) == 2:
        try:
            players_input = int(argv[1])
        except ValueError:
            exit(invalid_input_error)
        else:
            if players_input in [1, 2]:
                return players_input
            else:
                exit(invalid_input_error)
    elif len(argv) == 1:
        return 2
    else:
        exit(invalid_input_error)

def simulate_game(players):
    """
    This function manages the game rounds
    return value: "x" or "o" if a user wins, tie if tied

    it creates a table using the Table class
    then it loops for ever during each loop it calls either one/multiplayer round depending on the players
    finally it checks if the game ended if so it retruns the winner or tie
    """
    table = Table()
    print(table)

    # loop for ever
    while True:
        # simulate one/multi plyaer round (returns a table)
        if players in [1, 2]:
            table, game_state = simulate_round(table, players)
        else:
            raise ValueError("unexpected player's count (supposed to be 1 or 2)")

        # check if the game ended (!= None) if so return winner or tie

        if game_state != None:
            return game_state

def simulate_round(table, players_count):
    """
    this function simulates a round
    it accepts a table and players_count as input
    returns a list of table and game_state

    for each user this function:
    prompts user for notation if the player is a bot it asks the bot's function for notation
    it adds the player and his notation to the table
    finaly check if the game ended if so it retruns the winner and the table
    if it is the end of round it returns table and None
    """
    players = ["x", "o"]

    # for each player
    for player in players:
        # prompt the user for input
        while True:
            try:
                if players_count == 2 or (players_count == 1 and player == "x"):
                    notation = input(f"{player} turn: ")
                    game_state = table.add(notation, player)
                else:
                    print("bot turn")
                    game_state = table.add(bot(table.available), player)
            except:
                pass
            else:
                break

        # print table
        print(table)
        if game_state != None or player == "o":
            return [table, game_state]

def bot(available_notations):
    """
    accepts available notations as input
    returns one random notation of the avaiable notations
    choice is made using the random.choice library
    """
    return choice(available_notations)

if __name__ == "__main__":
    main()