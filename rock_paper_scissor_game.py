##################################### ROCK PAPER SCISSORS GAME USING TKINTER MODULE #######################################

from tkinter import *
import tkinter
import random
window=tkinter.Tk()
window.geometry("1200x800")
window.configure(bg='Mediumseagreen',highlightbackground="Black",highlightthickness = 30)
window.title("Rock_paper_scissors_game")
button1=Button(window,text="ROCK PAPER SCISSORS GAME",width=75,font=("Arial Bold",50),bd=8)
button2=Button(window,text="USER v/s COMPUTER",width=75,font=("Arial Bold",20),bd=8)
button1.config(bg='light green')
button2.config(bg='violet')
button1.pack()
button2.pack(pady=20)

computer_value =["Rock","Paper","Scissors"]

""" **********************************  function for if user want restart game *******************************************"""
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l3.config(text = "")
    l4.config(text = "")
 
""" **************************************** function for Rock choice **************************************************"""
def rock():
    computer_choice = computer_value[(random.randint(0,2))]
    if computer_choice == "Rock":
        winner= "Match Draw"
    elif computer_choice=="Scissor":
        winner= "User Win"
    else:
        winner= "Computer Win"
    l3.config(text = computer_choice)
    l4.config(text =winner)
    
""" **************************************** function for Paper choice ************************************************"""   
def paper():
    computer_choice= computer_value[(random.randint(0, 2))]
    if computer_choice== "Paper":
        winner= "Match Draw"
    elif computer_choice=="Scissor":
        winner= "Computer Win"
    else:
        winner= "User Win"
    l3.config(text = computer_choice)
    l4.config(text =winner)
    
""" **************************************** function for Scissor choice ************************************************"""  
def scissor():
    computer_choice= computer_value[(random.randint(0,2))]
    if computer_choice == "Rock":
        winner= "Computer Win"
    elif computer_choice== "Scissor":
        winner= "Match Draw"
    else:
        winner= "User Win"
    l3.config(text =computer_choice)
    l4.config(text =winner)

""" Button work"""
frame1 = Frame(window)
frame1.pack()
b1=Button(frame1,text="Rock",width=15,font=("Arial Bold",20),bd=12,command = rock)
b1.config(bg='red')

b2=Button(frame1,text="Paper",width=15,font=("Arial Bold",20),bd=12,command = paper)
b2.config(bg='green')

b3=Button(frame1,text="Scissors",width=15,font=("Arial Bold",20),bd=12,command = scissor)
b3.config(bg='blue')

b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)


l2= Button(window,text = "Computer choice showing in white Box",font = "normal 0 bold",bg = "pink",width = 75 ,borderwidth = 2,relief = "solid",bd=4)
l2.pack(pady = 20)

l3 = Label(window,text = "",font = "normal 20 bold",bg = "white",width = 15 ,borderwidth = 2,relief = "solid")
l3.pack(pady = 20)

l4 = Button(window,text = "",font = "normal 40 bold",bg = "yellow",width = 15 ,borderwidth = 5,bd=8,relief = "solid")
l4.pack(pady = 20)

Button(text="Restart",width=15,bg="DodgerBlue",font=("Arial Bold",20),bd=12,command = reset_game).pack(side='bottom')
window.mainloop()

