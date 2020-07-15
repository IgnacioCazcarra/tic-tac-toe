from tkinter import *
import tkinter.messagebox
import tkinter.font as font

turns = 0

def click(buttons):
    global turns,board
    if finished(board):
        disableButtons(board)
        tkinter.messagebox.showinfo("Tie","We have a tie")
    elif buttons["text"] == " " and turns%2==0:
        buttons["text"] = "X"
        turns+=1
        if(winner(board)):
            disableButtons(board)
            current = buttons["text"]
            tkinter.messagebox.showinfo("Game over",f"{current}'s player wins")

    elif buttons["text"] == " " and turns%2==1:
        buttons["text"] = "O"
        turns+=1
        if(winner(board)):
            disableButtons(board)
            current = buttons["text"]
            tkinter.messagebox.showinfo("Game over",f"{current}'s player wins")


def disableButtons(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j].configure(state=DISABLED)
            

def finished(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]["text"]==" ":
                return False
    return True


def winner(board):

    #Check row
    for i in range(len(board)):
        if board[i][0]["text"]==board[i][1]["text"]==board[i][2]["text"] and board[i][0]["text"]!=" ":
            return True
    
    #Check col
    for j in range(len(board[0])):
        if board[0][j]["text"]==board[1][j]["text"]==board[2][j]["text"] and board[0][j]["text"]!=" ":
            return True
    
    #Check both diag
    if board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"] and board[0][0]["text"]!=" ":
        return True
    
    if board[2][0]["text"]==board[1][1]["text"]==board[0][2]["text"] and board[2][0]["text"]!=" ":
        return True

    return False

    
root = Tk()

buttons = StringVar()
myFont = font.Font(size=20)

button1 = Button(root,text=" ",width=10,height=5, command=lambda: click(button1))
button1['font'] = myFont
button1.grid(row=0,column=0)

button2 = Button(root,text=" ",width=10,height=5, command=lambda: click(button2))
button2['font'] = myFont
button2.grid(row=0,column=1)

button3 = Button(root,text=" ",width=10,height=5, command=lambda: click(button3))
button3['font'] = myFont
button3.grid(row=0,column=2)

button4 = Button(root,text=" ",width=10,height=5, command=lambda: click(button4))
button4['font'] = myFont
button4.grid(row=1,column=0)

button5 = Button(root,text=" ",width=10,height=5, command=lambda: click(button5))
button5['font'] = myFont
button5.grid(row=1,column=1)

button6 = Button(root,text=" ",width=10,height=5, command=lambda: click(button6))
button6['font'] = myFont
button6.grid(row=1,column=2)

button7 = Button(root,text=" ",width=10,height=5, command=lambda: click(button7))
button7['font'] = myFont
button7.grid(row=2,column=0)

button8 = Button(root,text=" ",width=10,height=5, command=lambda: click(button8))
button8['font'] = myFont
button8.grid(row=2,column=1)

button9 = Button(root,text=" ",width=10,height=5, command=lambda: click(button9))
button9['font'] = myFont
button9.grid(row=2,column=2)

board = [[button1,button2,button3],[button4,button5,button6],[button7,button8,button9]]
            

if __name__ == "__main__":
    root.mainloop()