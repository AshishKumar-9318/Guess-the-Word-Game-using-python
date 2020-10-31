from tkinter import *
from tkinter import messagebox
from random import shuffle
from PIL import Image, ImageTk
import playsound
from threading import Thread
from time import sleep
import pygame
from tkinter import ttk

def progressbar():
	s = ttk.Style()
	# s.theme_use('clam')
	s.configure("white.Horizontal.TProgressbar", foreground='white', background='#1C1C1C')
	progress_bar = ttk.Progressbar(splash_root,style="white.Horizontal.TProgressbar", orient="horizontal",mode="determinate", length=303)
	progress_bar.pack()
	splash_root.update()
	progress_bar['value'] = 0
	splash_root.update()
 
	while progress_bar['value'] < 100:
		progress_bar['value'] += 1
		splash_percentage_label['text'] = str(progress_bar['value']) + ' %'
		splash_root.update()
		sleep(0.05)

def destroySplash():
	splash_root.destroy()

splash_root = Tk()
splash_root.configure(bg='#1C1C1C')
splash_root.overrideredirect(True)
splash_label = Label(splash_root, text="Processing...", font=('montserrat',15),bg='#1C1C1C',fg='white')
splash_label.pack(pady=40)

ph_symbol11 = Image.open('../image/first_symbol.png')
ph_symbol11 = ph_symbol11.resize((50, 50), Image.ANTIALIAS)
ph_symbol11 = ImageTk.PhotoImage(ph_symbol11)
symbol_root=Label(splash_root,image=ph_symbol11,bd=0,bg='#1C1C1C').place(x=170,y=65)
splash_percentage_label = Label(splash_root, text="0 %", font=('montserrat',15),bg='#1C1C1C',fg='white')
splash_percentage_label.pack(pady=(0,10))
w_width, w_height = 400, 200
s_width, s_height = splash_root.winfo_screenwidth(), splash_root.winfo_screenheight()
x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
splash_root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30))
progressbar()
splash_root.after(10, destroySplash)
splash_root.mainloop()




def four_frame_screen():
	import os 
	os.system('python main_frame.py')

def closegame(e):
	result = messagebox.askquestion('Alert', 'Are you sure you want to quit the game?')
	if result=='no': return
	quit()

def closegame():
	result = messagebox.askquestion('Alert', 'Are you sure you want to quit the game?')
	if result=='no': return
	quit()
root = Tk()
# root.geometry("1300x1100")
# w_width, w_height = 1300, 720 
# s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
# x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
# root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30))
# root.atributes("-Fullscreen",True)
root.attributes("-fullscreen",True)

wallframe=Frame(root)
wallframe.pack(fill=BOTH)

ph_wallframe = Image.open('../image/main_wallpaper_first.png')
ph_wallframe = ph_wallframe.resize((1300, 750), Image.ANTIALIAS)
ph_wallframe = ImageTk.PhotoImage(ph_wallframe)
Label(wallframe, image=ph_wallframe).pack(fill=BOTH)


# name_label=Label(wallframe,text='Word of Jungle',font=('Arial Bold', 100))
# name_label.place(x=150,y=100)


game_frame=Frame(wallframe, bg="purple")
game_frame.place(x=50,y=220)	

ph_button = Image.open('../image/main_start_button1.png')
ph_button = ph_button.resize((90, 90), Image.ANTIALIAS)
ph_button = ImageTk.PhotoImage(ph_button)
Button(root,text="    Start    ",font=('Arial', 20),image=ph_button,bg='#2E2E2E',bd=0,relief=FLAT,activebackground='#2E2E2E',command=four_frame_screen).place(x=600,y=498)
# Button(game_frame,text="    Start    ",font=('Arial', 20)).grid(row=0, column=1, ipadx=50, ipady=50, padx=20)
# Button(game_frame,text="    Start    ",font=('Arial', 20)).grid(row=0, column=2, ipadx=50, ipady=50, padx=20)
# Button(game_frame,text="    Start    ",font=('Arial', 20)).grid(row=0, column=3, ipadx=50, ipady=50, padx=20)


ph_quit = Image.open('../image/quit_button.png')
ph_quit = ph_quit.resize((50, 50), Image.ANTIALIAS)
ph_quit = ImageTk.PhotoImage(ph_quit)
Button(root,text='Quit',font=('Arial',10),command=closegame,image=ph_quit,bd=0,bg='black',activebackground='black').place(x=0,y=0)

# def playmusic():
# 	print('Music is started')
# 	playsound.playsound('WhatsApp Audio 2020-10-27 at 12.41.49 AM.mpeg')
# 	print('song is stopped')
# Thread(target=playmusic).start()
pygame.mixer.init()

def playmusic():
	song='WhatsApp Audio 2020-10-27 at 12.41.49 AM.mpeg'
	pygame.mixer.music.load(song)
	pygame.mixer.music.play(loops=0)

def stopmusic():
	pygame.mixer.music.stop()


ph_button_play = Image.open('../image/music_play_button.png')
ph_button_play = ph_button_play.resize((50, 50), Image.ANTIALIAS)
ph_button_play = ImageTk.PhotoImage(ph_button_play)

Button(root,text="PLAY",command=playmusic,image=ph_button_play,bd=0,bg='black',relief=FLAT,activebackground='black').place(x=1150,y=0)

ph_button_stop = Image.open('../image/music_stop_button.png')
ph_button_stop = ph_button_stop.resize((50, 50), Image.ANTIALIAS)
ph_button_stop = ImageTk.PhotoImage(ph_button_stop)
Button(root,text="STOP",command=stopmusic,image=ph_button_stop,bg='black',bd=0,relief=FLAT,activebackground='black').place(x=1210,y=0)
	
root.bind("<Escape>", closegame)
root.mainloop()