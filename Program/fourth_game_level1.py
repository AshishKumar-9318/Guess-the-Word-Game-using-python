import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle
from PIL import Image, ImageTk

root=Tk()
root.geometry("1200x1000")
root.attributes("-fullscreen",True)

def closegame(e):
	quit()

def clear():
	e1.delete(0,END)
	e2.delete(0,END)


def next_level_with_wrong():
	messagebox.showinfo("Next Level",'Next Level is Locked Firstly Solved this')

def next_level_with_right():
	import os
	os.system('python fourth_game_level2.py')
	quit()

def ans_check():
	user_answer1=e1.get()
	main_answer1='cap'
	user_answer2=e2.get()
	main_answer2='apple'
	if(user_answer2==main_answer2):
		if(user_answer1==main_answer1):
			messagebox.showinfo("Well Done",'You have a Right Answer')
			Button(root,text="      Next      ",font=('Arial',20),command=next_level_with_right,image=ph_next).place(x=1080,y=450)
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
	os.system('python hint_crossword_level1.py')

wallpaper_label=Label(root)
wallpaper_label.pack()

ph_wallpaper = Image.open('../image/first_game_wallpaper.png')
ph_wallpaper = ph_wallpaper.resize((1300, 720), Image.ANTIALIAS)
ph_wallpaper = ImageTk.PhotoImage(ph_wallpaper)
wallpaper_label.configure(image=ph_wallpaper)

frame1 = Frame(root, bg='White')
# frame2 = Frame(root, bg='green')
frame1.place(x=180,y=20)
# frame2.pack(fill=X, side=BOTTOM)

lb1=Label(frame1)
lb1.pack()


# OperationFrame = Frame(frame2, bg='blue',width=425,height=400)
# OperationFrame.grid(row=0,column=0)

# OperationFrame1 = Frame(frame2, bg='pink',width=425,height=400)
# OperationFrame1.grid(row=0,column=1)

# OperationFrame2 = Frame(frame2, bg='black',width=430,height=400)
# OperationFrame2.grid(row=0,column=2)



# leftframe = Frame(frame2, bg='blue', width=500, height=400)
# leftframe.pack()

e1=Entry(root,justify='center',font=('Arial',20))
e1.pack()
e1.place(height=40,width=300,x=480,y=400)
label_e1=Label(root,text="C _ P")
label_e1.pack()
label_e1.place(x=480,y=380)

e2=Entry(root,justify='center',font=('Arial',20))
e2.pack()
e2.place(height=40,width=300,x=480,y=500)
label_e2=Label(root,text="_ P _ _ E")
label_e2.pack()
label_e2.place(x=480,y=480)


ph_submit = Image.open('../image/submit.png')
ph_submit = ph_submit.resize((80, 80), Image.ANTIALIAS)
ph_submit = ImageTk.PhotoImage(ph_submit)

lb3=Label(root)
lb3.pack()
lb3.place(x=570,y=544)

Button(root,text="    Submit    ",font=('Arial', 20),command=ans_check,image=ph_submit).place(x=250,y=450)

ph_next = Image.open('../image/next.png')
ph_next = ph_next.resize((80, 80), Image.ANTIALIAS)
ph_next = ImageTk.PhotoImage(ph_next)

Button(root,text="      Next      ",font=('Arial',20),command=next_level_with_wrong,image=ph_next).place(x=1080,y=450)

ph_hint = Image.open('../image/hint.png')
ph_hint = ph_hint.resize((80, 80), Image.ANTIALIAS)
ph_hint = ImageTk.PhotoImage(ph_hint)

Button(root, text='     Hint     ', font=('Arial', 20),command=hint,image=ph_hint).place(x=940, y=450)

ph_quit = Image.open('../image/quit.png')
ph_quit = ph_quit.resize((80, 80), Image.ANTIALIAS)
ph_quit = ImageTk.PhotoImage(ph_quit)

Button(root, text='     Quit     ', font=('Arial', 20),command=lambda:quit(),image=ph_quit).place(x=110, y=450)

lb2=Label(frame1,text="   Level 1  ",font=('Arial 20'))
lb2.pack()
lb2.place(x=550,y=365)



ph = Image.open('../image/crossword1.jpeg')
ph = ph.resize((900, 300), Image.ANTIALIAS)
ph = ImageTk.PhotoImage(ph)
lb1.configure(image=ph)

ph_symbol = Image.open('../image/symbol.png')
ph_symbol = ph_symbol.resize((140, 140), Image.ANTIALIAS)
ph_symbol = ImageTk.PhotoImage(ph_symbol)

lb3.configure(image=ph_symbol,bd=0)
def open_home():
	import os
	os.system('python main_frame.py')
	quit()

ph_quit1 = Image.open('../image/home_button.png')
ph_quit1 = ph_quit1.resize((50, 50), Image.ANTIALIAS)
ph_quit1 = ImageTk.PhotoImage(ph_quit1)
Button(root,text="Home",command=open_home,font=('Arial',10),image=ph_quit1,bd=0,bg='black',activebackground='black').place(x=1220,y=00)
root.bind("<Escape>", closegame)
root.mainloop()