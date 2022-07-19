from cProfile import label
from tkinter import *
import random

from mysqlx import Result

root = Tk()
root.title("rock-paper-scissors game")
root.geometry("400x400")
root.resizable(0, 0)
root.configure(bg = "black")

Label(root, text = "rock-paper-scissors game", 
font = "arial 20 bold", bg = "black", fg = "white").pack()

user_take = StringVar()
Label(root, text="choose any one: rock, paper, scissors", 
font="arial 15 bold",bg="black",fg="blue").place(x = 16, y = 70)
Entry(root, font="arial 15 bold",
textvariable = user_take).place(x = 85, y = 130)

#computer choice
comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = "rock"
elif comp_pick == 2:
    comp_pick = "paper"
else:
    comp_pick = "scissors"

result = StringVar()
def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        result.set("draw")
    elif user_pick == "rock":
        if comp_pick == "paper":
            result.set("computer wins")
        else:
            result.set("user wins")
    elif user_pick == "paper":
        if comp_pick == "scissors":
            result.set("computer wins")
        else:
            result.set("user wins")
    elif user_pick == "scissors":
        if comp_pick == "rock":
            result.set("computer wins")
        else:
            result.set("user wins")
    else:
        result.set("invalid input")

def reset():
    result.set("")
    user_take.set("")
    
def quit():
    root.destroy()


Entry(root, font="arial 10 bold", textvariable=result,
 width=50).place(x = 25, y = 250)

Button(root, text="play", font="arial 13 bold",
 command=play).place(x = 170, y = 190)
    
Button(root, text="reset", font="arial 13 bold",
command=reset).place(x = 90, y = 310)

Button(root, text="quit", font="arial 13 bold",
command=quit).place(x = 250, y = 310)


root.mainloop()
