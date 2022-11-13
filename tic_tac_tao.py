def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    
    
    for i in (board):
        counter = 0
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for m in i:
            counter +=1 
            if counter == len(i):
                print("|  ",m,"  |")
            else:
                print("|  ",m,end="   ")
        print("|       |       |       |")
    print("+-------+-------+-------+")
        
    return board
            


def enter_move(board):
    c = -1
    move = int(input("Enter your move: "))
    while move <=0 or move >= 10:
                print("Enter a valid number greater than 0 and smaller than 10 !!")
                move = move = int(input("Enter your move: "))
    if move:
        for i in board:
            c += 1 
            for m in range(len(i)):
                if move == board[c][m]:
                    board[c][m] = "O"
    draw_move(board)
    return display_board(board)
    
        
        
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    pass


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board):
    from random import randrange
    
    
    c = -1

    
    move = (randrange(8))
    while move == 5:
        move = (randrange(8))
    
    if move:
        for i in board:
            c += 1 
            for m in range(len(i)):
                if move == board[c][m]:
                    board[c][m] = "X"
    
    return display_board(board)
    
    
        
    # The function draws the computer's move and updates the board.
    pass
board = [[1,2,3],[4,"X",6],[7,8,9]]

enter_move(board)
