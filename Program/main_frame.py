import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle
from PIL import Image, ImageTk

def closegame(e):
	quit()

def start_first_game():
	import os
	os.system('python second_game.py')

def start_second_game():
	import os
	os.system('python first_game.py')
def start_third_game():
	import os
	os.system('python third_game.py')

def start_fourth_game():
	import os
	os.system("python fourth_game_level1.py")
	# os.system('python ')
	# execfile('python_project_4_level1.py')
root=Tk()
root.geometry("1200x1000")
root.attributes("-fullscreen",True)
# root.wm_attributes('-transparentcolor',root['bg'])

frame1=Frame(root,bg="white")
frame1.pack(fill=X, side=TOP)

# lb1=Label(frame1,text="The Word of Jungle",font=('Arial 30'))
# lb1.pack()

frame2=Frame(root,bg="purple")
frame2.pack(fill=X,side=BOTTOM)	

ph_symbol = Image.open('../image/symbol_image.png')
ph_symbol = ph_symbol.resize((100, 100), Image.ANTIALIAS)
ph_symbol = ImageTk.PhotoImage(ph_symbol)


symbol_label=Label(root,image=ph_symbol,bd=0)
symbol_label.place(x=594.4,y=324)

OperationFrame = Frame(frame2, bg='black',width=640,height=360)
OperationFrame.grid(row=0,column=0)

lb_Operationframe=Label(OperationFrame)
lb_Operationframe.pack()
lb_Operationframe.place(x=20,y=20)

ph_button = Image.open('../image/start_button_1.png')
ph_button = ph_button.resize((100, 100), Image.ANTIALIAS)
ph_button = ImageTk.PhotoImage(ph_button)

Button(OperationFrame,text="Start",font=('Arial', 20),command=start_first_game,image=ph_button,bg='#ffe0bd',bd=0,relief=FLAT,activebackground='#ffe0bd').place(x=522,y=242)

ph_Operationframe = Image.open('../image/first_game_image.PNG')
ph_Operationframe = ph_Operationframe.resize((600, 320), Image.ANTIALIAS)
ph_Operationframe = ImageTk.PhotoImage(ph_Operationframe)
lb_Operationframe.configure(image=ph_Operationframe)

OperationFrame1 = Frame(frame2, bg='black',width=640,height=360)
OperationFrame1.grid(row=0,column=1)

lb_Operationframe1=Label(OperationFrame1)
lb_Operationframe1.pack()
lb_Operationframe1.place(x=20,y=20)

ph_button1 = Image.open('../image/start_button_2.png')
ph_button1 = ph_button1.resize((100, 100), Image.ANTIALIAS)
ph_button1 = ImageTk.PhotoImage(ph_button1)

Button(OperationFrame1,text="Start",font=('Arial', 20),command=start_second_game,image=ph_button1,bg='#ffe0bd',bd=0,relief=FLAT,activebackground='pink').place(x=20,y=242)

ph_Operationframe1 = Image.open('../image/second_game_image.png')
ph_Operationframe1 = ph_Operationframe1.resize((600, 320), Image.ANTIALIAS)
ph_Operationframe1 = ImageTk.PhotoImage(ph_Operationframe1)
lb_Operationframe1.configure(image=ph_Operationframe1)

OperationFrame2 = Frame(frame2, bg='black',width=640,height=360)
OperationFrame2.grid(row=1,column=0)

lb_Operationframe2=Label(OperationFrame2)
lb_Operationframe2.pack()
lb_Operationframe2.place(x=20,y=20)

ph_button2 = Image.open('../image/start_button_3.png')
ph_button2 = ph_button2.resize((100, 100), Image.ANTIALIAS)
ph_button2 = ImageTk.PhotoImage(ph_button2)

Button(OperationFrame2,text="Start",font=('Arial', 20),command=start_third_game,image=ph_button2,bg='#877070',bd=0,relief=FLAT,activebackground='#877070').place(x=519,y=22)


# Button(OperationFrame2,text="Start",font=('Arial', 20),command=start_third_game).place(x=430,y=130)

ph_Operationframe2 = Image.open('../image/third_game_image.png')
ph_Operationframe2 = ph_Operationframe2.resize((600, 320), Image.ANTIALIAS)
ph_Operationframe2 = ImageTk.PhotoImage(ph_Operationframe2)
lb_Operationframe2.configure(image=ph_Operationframe2)

OperationFrame3=Frame(frame2,bg='black',width=640,height=360)
OperationFrame3.grid(row=1,column=1)

lb_Operationframe3=Label(OperationFrame3)
lb_Operationframe3.pack()
lb_Operationframe3.place(x=20,y=20)

ph_button3 = Image.open('../image/start_button_4.png')
ph_button3 = ph_button3.resize((100, 100), Image.ANTIALIAS)
ph_button3 = ImageTk.PhotoImage(ph_button3)

Button(OperationFrame3,text="Start",font=('Arial', 20),command=start_fourth_game,image=ph_button3,bg='#ffe0bd',bd=0,relief=FLAT,activebackground='pink').place(x=20,y=20)


# Button(OperationFrame3,text="Start",font=('Arial', 20),command=start_fourth_game).place(x=170,y=130)

ph_Operationframe3 = Image.open('../image/fourth_game_image.png')
ph_Operationframe3 = ph_Operationframe3.resize((600, 320), Image.ANTIALIAS)
ph_Operationframe3 = ImageTk.PhotoImage(ph_Operationframe3)
lb_Operationframe3.configure(image=ph_Operationframe3)

# start_frame=Frame(root)
# start_frame.place(x=500,y=300)

ph_quit = Image.open('../image/quit_button.png')
ph_quit = ph_quit.resize((50, 50), Image.ANTIALIAS)
ph_quit = ImageTk.PhotoImage(ph_quit)
Button(root,text='Quit',font=('Arial',10),command=lambda:quit(),image=ph_quit,bd=0,bg='black',activebackground='black').place(x=0,y=0)

root.bind("<Escape>", closegame)
root.mainloop()