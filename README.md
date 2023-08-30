# Tic-Tac-Toe
## Video Demo: <https://watch.screencastify.com/v/G3wh8e0xLzYxluqjN3XY>
## Description:
The pythonic version of the famous two player game tic-tac-toe
## 1. How to use:
start by typing in the terminal
--python project.py n--
where n represents the number of players (1 or 2)
note that n is optional if not written the 2 player mode will be started
each player will be prompted to enter a notation
and if a player win he will get +1 to his score if they get a tie the will both get +1
in the end the player/s will be asked if they want to play again (y, yes) for accept and (n, no) for refuse
## 2. Technologies and libraries
- python
- tabulate library
- sys library
- random library
- pytest library
## 3. File Management
## 3. Table class
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
## 3.2 main Function
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
## 3.3 get_players Function
Get player function returns an int (1 or 2)
it returns number of players whom are going to play

it checks the user input if he inputed 1 or 2 it will be returned
if he didn't input anything 2 will be returned
if he inputs anyother thing the system will quit and show usage to user
## 3.4 simulate_game Function
This function manages the game rounds
return value: "x" or "o" if a user wins, tie if tied

it creates a table using the Table class
then it loops for ever during each loop it calls either one/multiplayer round depending on the players
finally it checks if the game ended if so it retruns the winner or tie
# 3.5 simulate_round Function
this function simulates a round
it accepts a table and players_count as input
returns a list of table and game_state

for each user this function:
prompts user for notation if the player is a bot it asks the bot's function for notation
it adds the player and his notation to the table
finaly check if the game ended if so it retruns the winner and the table
if it is the end of round it returns table and None
## 3.6 bot Function
accepts available notations as input
returns one random notation of the avaiable notations
choice is made using the random.choice library

## thanks for using Tic-Tac-Toe