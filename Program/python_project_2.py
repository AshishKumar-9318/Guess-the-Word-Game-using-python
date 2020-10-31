import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle
from PIL import Image, ImageTk

root = Tk()
root.geometry('1200x1000')
root.attributes("-fullscreen", True)

score=0
image_list=['ONION.PNG','potatoe.PNG','beetroot.PNG','capsicum.PNG','carrot.PNG','cauliflower.PNG','cucumber.PNG','eggplant.PNG','greenbean.PNG']
num=random.randint(0,len(image_list)-1)
print(num)

def clear():
    userAnswerField.delete(0,END)


def closeGame(e):
    quit()

def initial():
    lb2.configure(text="Score="+str(score))

def ans_check():
    global image_list,num,score
    name_image=image_list[num]
    user_input=userAnswerField.get()
    main,exten=name_image.split('.')
    if user_input.lower()==main.lower():
        messagebox.showinfo("Well Done",'You have a right answer')
        clear()
        score=score+1
        lb2.configure(text='Score='+str(score))
        Reset()
    else:
        messagebox.showinfo("Try Again","Better Luck next time")
        clear()

def Reset():
    global image_list,num
    num=random.randint(0,len(image_list)-1)
    ph = Image.open(image_list[num])
    ph = ph.resize((900, 300), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(ph)
    randomImgLbl.configure(image=ph)
    # randomImgLbl = Label(frame1, image=ph)
    # randomImgLbl.pack(padx=10, pady=10)  
    e1.delete(0,END)

wallpaper_label=Label(root)
wallpaper_label.pack()

ph_wallpaper = Image.open('first_game_wallpaper.png')
ph_wallpaper = ph_wallpaper.resize((1300, 720), Image.ANTIALIAS)
ph_wallpaper = ImageTk.PhotoImage(ph_wallpaper)
wallpaper_label.configure(image=ph_wallpaper)

frame1 = Frame(root)
# frame2 = Frame(root)
frame1.place(x=170,y=50)
# frame2.place(x=200,y=500)

randomImgLbl = Label(frame1)
randomImgLbl.pack(padx=10, pady=10)

# OperationFrame = Frame(frame2, width=500, height=400)
# OperationFrame.pack()

userAnswerField = Entry(root, font=('Arial', 20), bd=15, width=28, relief=FLAT)
userAnswerField.place(x=420, y=400)
userAnswerField.focus()

ph_check = Image.open('check.png')
ph_check = ph_check.resize((80, 80), Image.ANTIALIAS)
ph_check = ImageTk.PhotoImage(ph_check)


Button(root, text='Check', font=('Arial', 20),command=ans_check,image=ph_check).place(x=580, y=480)

ph_reset = Image.open('reset.png')
ph_reset = ph_reset.resize((80, 80), Image.ANTIALIAS)
ph_reset = ImageTk.PhotoImage(ph_reset)

Button(root, text=' Reset ', font=('Arial', 20), command=Reset,image=ph_reset).place(x=450, y=585)

ph_quit = Image.open('quit.png')
ph_quit = ph_quit.resize((80, 80), Image.ANTIALIAS)
ph_quit = ImageTk.PhotoImage(ph_quit)


Button(root,text="          Quit          ",command=lambda:quit(),font=('Arial',20),image=ph_quit).place(x=725,y=585)
# Button(OperationFrame,text='Clear',font=('Arial',20),command=clear).place(x=182,y=220)

lb2=Label(root,text='SCORE', font='Helvetica 40')
# lb2.pack(pady=5,ipady=10,ipadx=10)
lb2.place(x=552,y=-5)

ph = Image.open(image_list[num])
ph = Image.open(image_list[num])
ph = ph.resize((900, 300), Image.ANTIALIAS)
ph = ImageTk.PhotoImage(ph)
randomImgLbl.configure(image=ph)
# lb2.configure(text="Score="+str(score))
ph_symbol = Image.open('symbol.png')
ph_symbol = ph_symbol.resize((110, 110), Image.ANTIALIAS)
ph_symbol = ImageTk.PhotoImage(ph_symbol)
lb3=Label(root,bd=0)
lb3.place(x=575,y=580)
lb3.configure(image=ph_symbol)

initial()

root.bind('<Escape>', closeGame)
root.mainloop()