
def make_board():
    board=[ ["","",""],
            ["","",""],
            ["","",""],
    ]
    return board
def potental_moves(board):
    list1=[]
    for row in range(3):
        for col in range(3):
            if(board[row][col]==""):
                list1.append((row,col))
    return(list1)
var1=make_board()
print(var1)
var2=potental_moves(var1)
print(var2)
def print_board(board):
    for row in range(3):
        for col in range(3):
            print(board)


print_board(var1)
          
            