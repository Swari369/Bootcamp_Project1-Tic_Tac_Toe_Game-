"""
Requirements:
1. Users --> 2
    1.1 ask for symbol to users 'X' - 'O'
    1.2. if 2 users --> game start --> empty board
2. game rules:
    2.1. how to win? --> 8 ways
    2.2. If someone wins --> who win, final board
    2.3. If not from 8 ways of winning, and if everything is filled --> tie
    2.4 Input check --> for invalid input
3. Game logic:
    3.1 First display an empty board
    3.2 User 1 input 
        4.2.1 Check invalid input for user 1 --> if valid, go to user 2 --> Otherwise ask User 1 for another valid input
                valid input done --> output with displaying on board
    3.3 User 2 input
        4.3.1 Check invalid input for user 2 --> if valid, go to user 1 --> Otherwise ask User 2 for another valid input
                valid input done --> output with displaying on board
    ....
    ....
    ....
    ....
4. always check the 8 ways after User 1 gives 3 input --> use GAME RULES
    4.1 if win --> display who wins and game stop
    4.2 if no one wins --> continue game
    4.3 if everything filled --> tie
5. If someone wins --> Game stop completely --> give the output
    5.1 ask for another round --> if true then clear board and start it again.
"""
winning_pattern = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
#Function 1: To define users and symbols

def players():
    num_players = int(input("Please tell me how many person you are: "))

    #if-statement to check 2 players are there or not
    if num_players != 2:
        print("Only 2 person can play the game.")
        return None

    print("Game Start!")
    #Ask user name
    player_1 = input("Player 1 please write your name: ")
    player_2 = input("Player 2 please write your name: ")
    #Ask for symbols to users
    sym_1 = input("Player 1 select your symbol: ")
    sym_2 = input("Player 2 select your symbol: ")

    #creating a game board
    empty = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    empty_board = [print(n) for n in empty]
    """for n in empty:
        print(n)"""
    
    return player_1, player_2, sym_1, sym_2, empty_board

  
#Function 2: Game Rules
def game_logic(player, win_pattern):
    sorted_value = set(sorted(player))
    
    #to check the winning list nums with the total inputs from players
    for pattern in win_pattern:
        if all(num in sorted_value for num in pattern):
            """for num in pattern:
                num in sorted1"""
            print(f"Player 1 won. Here is the pattern {pattern}.")
            return True
        
    if len(player) >= 5:
        return print("No one wins. Game ties.")            
        
    print("Game is still on. Please go forward")
    return False



"""#Function 3: Game playing --> to ask for inputs and check whether it's valid or not

def game_play():
    pass

print() --> when game starts Display an empty board

user1_input --> ask for the input cehck validity and prints
empty_board --> update (if valid input)

user1_input --> ask for the input cehck validity and prints
empty_board --> update (if valid input)


is_game_finish = False

while not is_game_finish:
    if 

    else:
        is_game_finish


#Function 4: To check who wins or if game ties
    #after 3 inputs from User 1 --> use Function 2 to check

if user1_input >= 3:
    
    if call game_logic() --> user 1 is not wins and 
    
    if wins --> who wins and final board
    else --> tie and board display

#Function 4: Game play

def start_game():
    
    users
    
    game_play

    
"""
