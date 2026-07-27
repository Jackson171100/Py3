
def make_board():
    board=[ ["","",""],
            ["","",""],
            ["","",""],
    ]
    return board
def potental_moves(board):
    for row in range(3):
        for col in range(3):
            if(board[row][col]==""):
                list1=[]
                list1.append((row,col))
                return(list1)
var1=make_board()
print(var1)
var2=potental_moves(var1)
print(var2)
 
          
            