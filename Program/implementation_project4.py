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
def ans_check():
    if(a=='1'):
        user_answer1=e1.get()
        main_answer1='cap'
        user_answer2=e2.get()
        main_answer2='apple'
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
def next_level_with_wrong():
    num=num+1
def hint():
    pass
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

Button(OperationFrame,text="    Submit    ",font=('Arial', 20),command=ans_check).place(x=130,y=60)
Button(OperationFrame,text="      Next      ",font=('Arial',20),command=next_level_with_wrong).place(x=130,y=180)
Button(OperationFrame2, text='     Hint     ', font=('Arial', 20),command=hint).place(x=140, y=60)
Button(OperationFrame2, text='     Quit     ', font=('Arial', 20),command=lambda:quit()).place(x=140, y=180)



list_image=['1.jpeg','2.guitar.chimpanzee.jpeg','3.cake.balloons.pink.jpeg','4.sunglasses.scarf.camera.jpeg']
num=0
print(list_image[num])

a,b=list_image[num].split('.')
if(a=='1'):
    ph = Image.open(list_image[num])
    ph = ph.resize((1200, 400), Image.ANTIALIAS)
    ph = ImageTk.PhotoImage(ph)
    lb1.configure(image=ph)

    e1=Entry(OperationFrame1)
    e1.pack()
    e1.place(height=40,width=300,x=65,y=50)
    label_e1=Label(OperationFrame1,text="C _ P")
    label_e1.pack()
    label_e1.place(x=65,y=30)

    e2=Entry(OperationFrame1)
    e2.pack()
    e2.place(height=40,width=300,x=65,y=200)
    label_e2=Label(OperationFrame1,text="_ P _ _ E")
    label_e2.pack()
    label_e2.place(x=65,y=180)

root.bind('<Escape>',closegame)
root.mainloop()