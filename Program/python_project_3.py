import tkinter
from tkinter import*
import random
from tkinter import messagebox
from random import shuffle

score=0

vowels = "aeiou"
word_without_vowel=[]
answer=['python','youtube','samosa','india','google','coffee','coronavirus','bacteria','netflix','alcohol']
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
	if user_input==answer[num]:
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
root.attributes("-fullscreen",True)

lb1= Label(root,font='Helvetica 100')
lb1.pack(pady=10,ipady=20,ipadx=10)

lb2=Label(root,font='Helvetica 40')
lb2.pack(pady=5,ipadx=10,ipady=10)

# lb2=Label(root,font='aries 10')
# lb2.pack(pady=5,ipady=2,ipadx=2)

final_answer=StringVar()
e1=Entry(root)
e1.pack(ipady=5,ipadx=5)

button1=Button(root,text="        Check        ",command=ans_check,font=('Arial',20))
button1.pack(pady=40)

button2=Button(root,text="        Reset        ",command=Reset,font=('Arial',20))
button2.pack()

Button(root,text="          Quit          ",command=lambda:quit(),font=('Arial',20)).place(x=525,y=570)

initial()
root.bind('<Escape>',closegame)
root.mainloop()

