import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle
from PIL import Image, ImageTk


# def raise_frame(frame):
# 	frame.tkraise()
def open_fruits():
	import os
	os.system('python second_game_fruits.py')
def open_sports():
	import os
	os.system('python second_game_sports.py')
def open_vegetables():
	import os
	os.system('python second_game_vegatebles.py')
def open_country():
	import os
	os.system('python second_game_country.py')
def open_rivers():
	import os
	os.system('python second_game_rivers.py')
def open_avengers():
	import os
	os.system('python second_game_avenger.py')
def open_computer_languages():
	import os
	os.system('python second_game_computer_languages.py')
def open_languages():
	import os
	os.system('python second_game_languages.py')
def closegame(e):
	quit()

root=tkinter.Tk()
w_width, w_height = 1200, 600 
s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30))
# root.atributes("-Fullscreen",True)
root.attributes("-fullscreen",True)

wallpaper_label=Label(root)
wallpaper_label.pack()


ph_wallpaper = Image.open('../image/Category.png')
ph_wallpaper = ph_wallpaper.resize((1300, 720), Image.ANTIALIAS)
ph_wallpaper = ImageTk.PhotoImage(ph_wallpaper)
wallpaper_label.configure(image=ph_wallpaper)


ph_button1 = Image.open('../image/Fruits.png')
ph_button1 = ph_button1.resize((150, 150), Image.ANTIALIAS)
ph_button1 = ImageTk.PhotoImage(ph_button1)

Button(root,text="Start",font=('Arial', 20),image=ph_button1,bg='black',bd=0,relief=FLAT,activebackground='black',command=open_fruits).place(x=100,y=50)

ph_button2 = Image.open('../image/sports.png')
ph_button2 = ph_button2.resize((150, 150), Image.ANTIALIAS)
ph_button2 = ImageTk.PhotoImage(ph_button2)

Button(root,text="Start",font=('Arial', 20),image=ph_button2,bg='black',bd=0,relief=FLAT,activebackground='black',command=open_sports).place(x=400,y=50)

ph_button3 = Image.open('../image/vegetables.png')
ph_button3 = ph_button3.resize((150, 150), Image.ANTIALIAS)
ph_button3 = ImageTk.PhotoImage(ph_button3)

Button(root,text="Start",font=('Arial', 20),image=ph_button3,bg='black',bd=0,relief=FLAT,activebackground='black',command=open_vegetables).place(x=700,y=50)

ph_button4 = Image.open('../image/languages.png')
ph_button4 = ph_button4.resize((150, 150), Image.ANTIALIAS)
ph_button4 = ImageTk.PhotoImage(ph_button4)

Button(root,text="Start",font=('Arial', 20),image=ph_button4,bg='black',bd=0,relief=FLAT,activebackground='black',command=open_languages).place(x=1000,y=50)

ph_button5 = Image.open('../image/computer_languages.png')
ph_button5 = ph_button5.resize((150, 150), Image.ANTIALIAS)
ph_button5 = ImageTk.PhotoImage(ph_button5)

Button(root,text="Start",font=('Arial', 20),image=ph_button5,bg='black',bd=0,relief=FLAT,activebackground='black',command=open_computer_languages).place(x=100,y=520)

ph_button6 = Image.open('../image/rivers.png')
ph_button6 = ph_button6.resize((150, 150), Image.ANTIALIAS)
ph_button6 = ImageTk.PhotoImage(ph_button6)

Button(root,text="Start",font=('Arial', 20),image=ph_button6,bg='black',bd=0,relief=FLAT,activebackground='black',command=open_rivers).place(x=400,y=520)

ph_button7 = Image.open('../image/avengers.png')
ph_button7 = ph_button7.resize((150, 150), Image.ANTIALIAS)
ph_button7 = ImageTk.PhotoImage(ph_button7)

Button(root,text="Start",font=('Arial', 20),image=ph_button7,bg='black',bd=0,relief=FLAT,activebackground='black',command=open_avengers).place(x=700,y=520)

ph_button8 = Image.open('../image/country.png')
ph_button8 = ph_button8.resize((150, 150), Image.ANTIALIAS)
ph_button8 = ImageTk.PhotoImage(ph_button8)

Button(root,text="Start",font=('Arial', 20),image=ph_button8,bg='black',bd=0,relief=FLAT,activebackground='black',command=open_country).place(x=1000,y=520)
ph_quit1 = Image.open('../image/home_button.png')
ph_quit1 = ph_quit1.resize((50, 50), Image.ANTIALIAS)
ph_quit1 = ImageTk.PhotoImage(ph_quit1)
# Button(root,text='Quit',font=('Arial',10),command=lambda:quit(),image=ph_quit21,bd=0,bg='black',activebackground='black').place(x=0,y=0)
Button(root,text='Home',font=('Arial',10),command=lambda:quit(),image=ph_quit1,bd=0,bg='black').place(x=1220,y=0)
ph_quit2 = Image.open('../image/quit_button.png')
ph_quit2 = ph_quit2.resize((50, 50), Image.ANTIALIAS)
ph_quit2 = ImageTk.PhotoImage(ph_quit2)
Button(root,text='Quit',font=('Arial',10),command=lambda:quit(),image=ph_quit2,bd=0,bg='black',activebackground='black').place(x=0,y=0)
root.bind("<Escape>",closegame)
root.mainloop()