import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle
from PIL import Image, ImageTk

root_hint=Tk()
root_hint.geometry("1200x1000")
root_hint.attributes("-fullscreen",True)

def back():
	# import os
	# os.system('python python_project_4.py')
	quit()

def closegame(e):
	quit()
frame1_hint = Frame(root_hint, bg='White')
# frame2 = Frame(root, bg='green')
frame1_hint.pack(fill=X, side=TOP)
# frame2.pack(fill=X, side=BOTTOM)

lb1=Label(frame1_hint)
lb1.pack()


ph = Image.open('../image/hint5.jpeg')
ph = ph.resize((1600, 800), Image.ANTIALIAS)
ph = ImageTk.PhotoImage(ph)
lb1.configure(image=ph)

button1=Button(frame1_hint,text="Back",font=('Arial',30),command=back)
button1.pack()
button1.place(x=300,y=639)

button2=Button(frame1_hint,text="Quit",font=('Arial',30),command=lambda:quit())
button2.pack()
button2.place(x=900,y=639)


root_hint.bind("<Escape>", closegame)
root_hint.mainloop()
