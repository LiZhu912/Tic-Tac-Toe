# Author: Li Qian Zhu
# This program is a simple command line tic-tac-toe game.

# Set up the board.
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# Initialize X and O symbols.
X = "X"
O = "O"

# Display the game board and position reference board.
def display_board():
    print(board[0],"|",board[1],"|",board[2]+"\t"+"1","|","2","|","3"+"\n"+
        board[3],"|",board[4],"|",board[5]+"\t"+"4","|","5","|","6"+"\n"+
        board[6],"|",board[7],"|",board[8]+"\t"+"7","|","8","|","9")

# Start the game.
def start_game():
    game_ongoing = True
    display_board()
    
    while game_ongoing:
        handle_turn(X)
        display_board()
        if check_win(X) == True:
            game_ongoing = False
            print("X won the game!")
            break
        if check_tie() == True:
            print("Match tied")
            break
        handle_turn(O)
        display_board()
        if check_win(O) == True:
            game_ongoing = False
            print("O won the game!")
            break
        if check_tie() == True:
            print("Match tied!")
            break
         
# Handle each player's turn.
def handle_turn(current_player):
    while True:
        position = input(current_player+"'s Turn. Pick a position from 1-9: ")

        # Check if input is an int.
        try:
            if isinstance(int(position),int):
                pass
        except:
            print("Invalid position type")
            continue
                  
        # Check if input is in range.
        if int(position) >=1 and int(position) <=9:
            position = int(position)-1
        else:
            print("Invalid range of position")
            continue
            
        # Check if the cell is empty.
        if board[position] == "-":
            board[position] = current_player
            break
        else:
            print("This position is already chosen")
            
def check_win(current_player):
    
    #Check Rows.
    if board[0]== current_player and board[1] == current_player and board[2] == current_player:
        return True
    elif board[3]== current_player and board[4] == current_player and board[5] == current_player:
        return True
    elif board[6]== current_player and board[7] == current_player and board[8] == current_player:
        return True

    #Check Columns.
    elif board[0]== current_player and board[3] == current_player and board[6] == current_player:
        return True
    elif board[1]== current_player and board[4] == current_player and board[7] == current_player:
        return True
    elif board[2]== current_player and board[5] == current_player and board[8] == current_player:
        return True

    #Check Diagonals.
    elif board[0]== current_player and board[4] == current_player and board[8] == current_player:
        return True
    elif board[2]== current_player and board[4] == current_player and board[6] == current_player:
        return True
    
    else:
        return False
# Check if there is a tie.
def check_tie():
    if "-" not in board:
        return True
    else:
        False
    
start_game()
