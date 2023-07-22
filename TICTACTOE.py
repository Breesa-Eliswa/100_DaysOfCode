board=["-", "-", "-",
       "-", "-", "-",
       "-", "-", "-" ]

CurrentPlayer ="X"
winner = None
gamerunning = True

def printboard(board):
    print(board[0]+ "|" +board[1]+ "|" +board[2])
    print("-----")
    print(board[3]+ "|" +board[4]+ "|" +board[5])
    print("-----")
    print(board[6]+ "|" +board[7]+ "|" +board[8])
#printboard(board)
def playerinputboard(board):
    inp=int(input("Enter a number from 1 to 9: "))
    if inp>=1 and inp<=9 and board[inp-1]=="-":
        board[inp-1]=CurrentPlayer
    else:
        print("Oops that position is already occupied !!...")

def horizontal_check(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!="-":
        winner = board[0]
        return True 
    elif board[3]==board[4]==board[5]and board[3]!="-":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8]and board[6]!="-": 
        winner = board[6]
        return True 

def vertical_check(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner = board[0]
        return True 
    elif board[1]==board[4]==board[7]and board[1]!="-":
        winner = board[1]
        return True
    elif board[2]==board[5]==board[8]and board[2]!="-": 
        winner = board[2]
        return True 

def diagonal_check(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner = board[0]
        return True 
    elif board[2]==board[4]==board[6]and board[2]!="-":
        winner = board[2]
        return True
    
def tie_check(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("Its a tie!!..")
        gamerunning = False

def win_check(board):
    if horizontal_check(board) or vertical_check(board) or diagonal_check(board):
        print(f"The winner is {winner}")


def switch_player():
    global CurrentPlayer
    if CurrentPlayer=="X":
        CurrentPlayer="O" 
    else:
        CurrentPlayer ="X"     

while gamerunning:
    printboard(board)
    playerinputboard(board)
    win_check(board)
    tie_check(board)
    switch_player()


