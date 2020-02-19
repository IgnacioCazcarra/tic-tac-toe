board = [
    [0,0,0],
    [0,0,0],
    [0,0,0]]


def draw_board(board):
    for i in range(len(board)):
        if i>0:
            print("\n-----------")
        for j in range(len(board[0])):
            if j!=0 and j!=3:
                print(" | ",end="")
                print(str(board[i][j]) + " ",end="")
            else: 
                print(str(board[i][j]) + " ",end="")


def play(board,player_char):
    col = -1
    row = -1
    while (col > 2 or col < 0):
        col = input("En que columna quiere posicionar la ficha {}?".format(player_char))
        if col.isdigit():
            col = int(col)
        else: col = -1
    while (row > 2 or row < 0):    
        row = input("En que fila quiere posicionar la ficha {}?".format(player_char))
        if row.isdigit():
            row = int(row)
        else: row = -1
    if (board[col][row] != "X") and (board[col][row] != "O"):
        board[col][row] = player_char
        return True


def finished(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                return False
    return True


def winner(board):

    #Check row
    for i in range(len(board)):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=0:
            return True
    
    #Check col
    for j in range(len(board[0])):
        if board[0][j]==board[1][j]==board[2][j] and board[0][j]!=0:
            return True
    
    #Check both diag
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=0:
        return True
    
    if board[2][0]==board[1][1]==board[0][2] and board[2][0]!=0:
        return True

    return False

    
def tic_tac_toe():
    turns = 0
    player_char = 0

    while not winner(board) and not finished(board):
        
        draw_board(board)
        
        print("\n************")
        
        player_char = "X" if turns%2==0 else "O"
        
        if play(board,player_char):
            turns+=1
            
    if winner(board):
        print("\n\tTenemos un ganador!\n\Felicitaciones jugador {} por haber ganado este juego\n".format(player_char))
    else: print("\n\t Señoras y señores, tenemos un empate!\n")
    draw_board(board)
            

if __name__ == "__main__":
    tic_tac_toe()