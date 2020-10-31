import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle
from PIL import Image, ImageTk

root=Tk()
root.geometry("1200x1000")
root.attributes("-fullscreen",True)

def next_level_with_wrong():
	messagebox.showinfo("Next Level",'Next Level is Locked Firstly Solved this')

def next_level_with_right():
	import os
	os.system('python python_project_4_level3.py')
	quit()

def closegame(e):
	quit()

def clear():
	e1.delete(0,END)
	e2.delete(0,END)

def ans_check():
	user_answer1=e1.get()
	main_answer1='guitar'
	user_answer2=e2.get()
	main_answer2='chimpanzee'
	if(user_answer2==main_answer2):
		if(user_answer1==main_answer1):
			messagebox.showinfo("Well Done",'You have a Right Answer')
			Button(OperationFrame,text="      Next      ",font=('Arial',20),command=next_level_with_right).place(x=130,y=180)
			clear()
			hint()
		else:
			messagebox.showinfo("Nope",'Better Luck Next Time')
			clear()
	else:
		messagebox.showinfo("Nope",'Better Luck Next Time')
		clear()

def hint():
	import os
	os.system('python hint_crossword_level2.py')

frame1 = Frame(root, bg='White')
frame2 = Frame(root, bg='green')
frame1.pack(fill=X, side=TOP)
frame2.pack(fill=X, side=BOTTOM)

lb1=Label(frame1)
lb1.pack()


OperationFrame = Frame(frame2, bg='blue',width=425,height=400)
OperationFrame.grid(row=0,column=0)

OperationFrame1 = Frame(frame2, bg='pink',width=425,height=400)
OperationFrame1.grid(row=0,column=1)

OperationFrame2 = Frame(frame2, bg='black',width=430,height=400)
OperationFrame2.grid(row=0,column=2)



# leftframe = Frame(frame2, bg='blue', width=500, height=400)
# leftframe.pack()

e1=Entry(OperationFrame1)
e1.pack()
e1.place(height=40,width=300,x=65,y=50)
label_e1=Label(OperationFrame1,text="G _ I _ A _")
label_e1.pack()
label_e1.place(x=65,y=30)


e2=Entry(OperationFrame1)
e2.pack()
e2.place(height=40,width=300,x=65,y=200)
label_e2=Label(OperationFrame1,text="C _ I _ P _ N Z _ _")
label_e2.pack()
label_e2.place(x=65,y=180)


Button(OperationFrame,text="    Submit    ",font=('Arial', 20),command=ans_check).place(x=130,y=60)
Button(OperationFrame,text="      Next      ",font=('Arial',20),command=next_level_with_wrong).place(x=130,y=180)
Button(OperationFrame2, text='Next Level', font=('Arial', 20)).place(x=140, y=60)
Button(OperationFrame2, text='     Hint     ', font=('Arial', 20),command=hint).place(x=140, y=60)
Button(OperationFrame2, text='     Quit     ', font=('Arial', 20),command=lambda:quit()).place(x=140, y=180)

lb2=Label(frame1,text="   Level 2  ",font=('Arial 20'))
lb2.pack()
lb2.place(x=550,y=365)



ph = Image.open('crossword2.jpeg')
ph = ph.resize((1200, 400), Image.ANTIALIAS)
ph = ImageTk.PhotoImage(ph)
lb1.configure(image=ph)

root.bind("<Escape>", closegame)
root.mainloop()