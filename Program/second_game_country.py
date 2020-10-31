import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle
from PIL import Image, ImageTk
import json
score=0

words=[]
answer=[]
data = json.load(open('word_collection.json', encoding='utf-8'))
def getlist(category):
    collection=data[category]
    for word in collection:
        answer.append(word)

getlist('country')

vowels = "aeiou"
word_without_vowel=[]

for i in range(len(answer)):
    word =answer[i]
    new_word = []
    for letter in word:
        if letter in vowels:
            new_word.append('_')
        else:
            new_word.append(letter)
    word_without_vowel.append(new_word)
# print(word_without_vowel)
num=random.randint(0,len(answer)-1)

def closegame(e):
    quit()

def initial():
    global words,answer,num,score
    lb1.configure(text=word_without_vowel[num])
    lb2.configure(text='Score='+str(score))


def ans_check():
    global words,num,answer,score
    user_input=e1.get()
    if user_input.lower()==answer[num].lower():
        messagebox.showinfo("Success","yup this is right")
        score=score+1
        lb2.configure(text='Score='+str(score))
        Reset()
    else:
        messagebox.showinfo("Error","nope this is not right")
        e1.delete(0,END)
        Reset()

def Reset():
    global words,answer,num
    num=random.randint(0,len(word_without_vowel)-1)
    lb1.configure(text=word_without_vowel[num])
    e1.delete(0,END)
root=tkinter.Tk()
w_width, w_height = 1200, 600 
s_width, s_height = root.winfo_screenwidth(), root.winfo_screenheight()
x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
root.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30))
# # root.atributes("-Fullscreen",True)
root.attributes("-fullscreen",True)
# # root.pack(bg='pink')
wallpaper_label=Label(root)
wallpaper_label.pack()

ph_wallpaper = Image.open('../image/first_game_wallpaper.png')
ph_wallpaper = ph_wallpaper.resize((1300, 720), Image.ANTIALIAS)
ph_wallpaper = ImageTk.PhotoImage(ph_wallpaper)
wallpaper_label.configure(image=ph_wallpaper)

word_frame=Frame(root)
word_frame.pack()
word_frame.place(x=0,y=100,height=200,width=1280)


lb1= Label(word_frame,font='Helvetica 100')
lb1.pack(pady=10,ipady=20,ipadx=10)
# lb1.place(x=200,y=200)

lb2=Label(root,font='Helvetica 40')
lb2.pack(pady=5,ipadx=10,ipady=10)
lb2.place(x=520,y=40)

lb3=Label(root)
lb3.pack()
lb3.place(x=570,y=544)

# lb2=Label(root,font='aries 10')
# lb2.pack(pady=5,ipady=2,ipadx=2)

final_answer=StringVar()
e1=Entry(root,justify='center',font=('Arial',20))
e1.pack(ipady=5,ipadx=5)
e1.place(x=420,y=320,width=400,height=50)

ph_check = Image.open('../image/check.png')
ph_check = ph_check.resize((100, 100), Image.ANTIALIAS)
ph_check = ImageTk.PhotoImage(ph_check)

button1=Button(root,text="        Check        ",command=ans_check,font=('Arial',20),image=ph_check)
button1.pack(pady=40)
button1.place(x=585,y=400)

ph_reset = Image.open('../image/reset.png')
ph_reset = ph_reset.resize((100, 100), Image.ANTIALIAS)
ph_reset = ImageTk.PhotoImage(ph_reset)


button2=Button(root,text="        Reset        ",command=Reset,font=('Arial',20),image=ph_reset)
button2.pack()
button2.place(x=450,y=565)

ph_quit = Image.open('../image/quit.png')
ph_quit = ph_quit.resize((100, 100), Image.ANTIALIAS)
ph_quit = ImageTk.PhotoImage(ph_quit)


Button(root,text="          Quit          ",command=lambda:quit(),font=('Arial',20),image=ph_quit).place(x=725,y=565)


ph_symbol = Image.open('../image/symbol.png')
ph_symbol = ph_symbol.resize((140, 140), Image.ANTIALIAS)
ph_symbol = ImageTk.PhotoImage(ph_symbol)

lb3.configure(image=ph_symbol,bd=0)
initial()
def open_home():
    import os
    os.system('python main_frame.py')
    quit()

ph_quit1 = Image.open('../image/home_button.png')
ph_quit1 = ph_quit1.resize((50, 50), Image.ANTIALIAS)
ph_quit1 = ImageTk.PhotoImage(ph_quit1)
Button(root,text="Home",command=open_home,font=('Arial',10),image=ph_quit1,bd=0,bg='black',activebackground='black').place(x=1220,y=00)
root.bind("<Escape>",closegame)
root.mainloop()