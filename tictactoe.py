import os

player1, player2 = '',''
input_row, input_column = '',''
previous_player = ''
player1_turn, player2_turn, = True, False

row_divider = "------+-------+------"
top_left = "     " 
top_middle = "     "
top_right = "     "
middle_left = "     "
middle_middle = "     "
middle_right = "     "
bottom_left = "     "
bottom_middle = "     "
bottom_right = "     "

#prints the current board
def printBoard():
    print(top_left,"|",top_middle,"|",top_right)
    print(row_divider)
    print(middle_left,"|",middle_middle,"|",middle_right)
    print(row_divider)
    print(bottom_left,"|",bottom_middle,"|",bottom_right)
    """
    print("  X  ","|","  X  ","|","  X  ")
    print("------+-------+--------")
    print("  X  ","|","  X  ","|","  X  ")
    print("------+-------+--------")
    print("  X  ","|","  X  ","|","  X  ")
    """

#takes player input and udpates the board to show changes
def updateBoard(player,input_row, input_column):
    global player1_turn, player2_turn
    global top_left, top_middle,top_right
    global middle_left, middle_middle, middle_right
    global bottom_left, bottom_middle, bottom_right

    if input_row == 'top':
        if input_column == 'left':
            top_left = top_left[:2] + player + top_left[3:]
        elif input_column == 'middle':
            top_middle = top_middle[:2] + player + top_middle[3:]
        else:
            top_right = top_right[:2] + player + top_right[3:]
    elif input_row == 'middle':
        if input_column == 'left':
            middle_left = middle_left[:2] + player + middle_left[3:]
        elif input_column == 'middle':
            middle_middle = middle_middle[:2] + player + middle_middle[3:]
        else:
            middle_right = middle_right[:2] + player + middle_right[3:]
    elif input_row == 'bottom':
        if input_column == 'left':
            bottom_left = bottom_left[:2] + player + bottom_left[3:]
        elif input_column == 'middle':
            bottom_middle = bottom_middle[:2] + player + bottom_middle[3:]
        else:
            bottom_right = bottom_right[:2] + player + bottom_right[3:]
    
    if player =='X' and player1 == 'X':
        player1_turn = False
        player2_turn = True
    elif player == 'O' and player1 == 'X':
        player2_turn = False
        player1_turn = True
    elif player == 'X' and player2 == "X":
        player2_turn = False
        player1_turn = True
    elif player == "O" and player2 == 'X':
        player1_turn = False
        player2_turn = True

    printBoard()
    
#check to see if there is a winner and end the game
def checkBoard(player):

    if top_left.strip() == "X" and top_middle.strip() == "X" and top_right.strip() == "X":
        if player1 == "X":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if middle_left.strip() == "X" and middle_middle.strip() == "X" and middle_right.strip() == "X":
        if player1 == "X":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if bottom_left.strip() == "X" and bottom_middle.strip() == "X" and bottom_right.strip() == "X":
        if player1 == "X":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_left.strip() == "X" and middle_middle.strip() == "X" and bottom_right.strip() == "X":
        if player1 == "X":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_right.strip() == "X" and middle_middle.strip() == "X" and bottom_left.strip() == "X":
        if player1 == "X":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_left.strip() == "X" and middle_left.strip() == "X" and bottom_left.strip() == "X":
        if player1 == "X":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_middle.strip() == "X" and middle_middle.strip() == "X" and bottom_middle.strip() == "X":
        if player1 == "X":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_right.strip() == "X" and middle_right.strip() == "X" and bottom_right.strip() == "X":
        if player1 == "X":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True



    if top_left.strip() == "O" and top_middle.strip() == "O" and top_right.strip() == "O":
        if player1 == "O":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if middle_left.strip() == "O" and middle_middle.strip() == "O" and middle_right.strip() == "O":
        if player1 == "O":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if bottom_left.strip() == "O" and bottom_middle.strip() == "O" and bottom_right.strip() == "O":
        if player1 == "O":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_left.strip() == "O" and middle_middle.strip() == "O" and bottom_right.strip() == "O":
        if player1 == "O":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_right.strip() == "O" and middle_middle.strip() == "O" and bottom_left.strip() == "O":
        if player1 == "":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_left.strip() == "O" and middle_left.strip() == "O" and bottom_left.strip() == "O":
        if player1 == "O":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_middle.strip() == "O" and middle_middle.strip() == "O" and bottom_middle.strip() == "O":
        if player1 == "O":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True
    if top_right.strip() == "O" and middle_right.strip() == "O" and bottom_right.strip() == "O":
        if player1 == "O":
            print("Player 1 wins!, Congratulations!")
            return True
        else:
            print("Player 2 wins!, Congratulations!")
            return True

    return False

            

#decide the players
def choosePlayer():
    global player1, player2
    player1 = input("Player 1 can choose X or O: \n")
    if player1.upper().strip() == "X":
        player2 = "O"
    else:
        player2 = "X"
        player1 = "O"

#determine player input location
def input_placement(current_player):
    
    input_row = str(input("Please choose which row you want to mark: top, middle, or bottom: \n"))
    input_column = str(input("Please choose which column to want to mark: left, middle, or right: \n"))

    if (input_row not in ['top','middle', 'bottom']) or (input_column not in ['left','middle','right']):
        print('You did not enter a valid choice, please try again: ')
        return False, False

    os.system("cls")
    return input_row, input_column


#runs the actual game
print("Welcome to Tic Tac Toe!")
p = choosePlayer()
while checkBoard(p) is False:
    if player1_turn is False:
        row, column = input_placement(player2)
        if row is False or column is False:
            continue
        else:
            updateBoard(player2,row, column)
    else:
        row, column = input_placement(player1)
        if row is False or column is False:
            continue
        else:
            updateBoard(player1,row, column)
    
    

