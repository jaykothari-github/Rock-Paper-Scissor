from tkinter import *
from random import choice

rw= Tk()
rw.geometry('600x400+300+100')
rw.title('Rock Paper Scissor')
rw.resizable(width=False,height=False)

lt = ["Rock", "Paper", "Scissor"]

u_count = 0
c_count = 0
u_w = IntVar()
c_w = IntVar()
uc = StringVar()
cc = StringVar()
res = StringVar()


def c(u_c):
    global u_count
    global c_count
    
    

    c_c = choice(lt)
    cc.set(c_c)
    uc.set(u_c)

    if c_c == u_c :
        res.set("It's Tie!!")

    elif c_c == "Rock" and u_c == "Paper":
        res.set("Yaaah hooo!! Player Win!!")
        u_count+=1
        u_w.set(u_count)
        
    
    elif c_c == "Paper" and u_c == "Scissor":
        res.set("Yaaah hooo!! Player Win!!")
        u_count+=1
        u_w.set(u_count)

    elif c_c == "Scissor" and u_c == "Rock" :
        res.set("Yaaah hooo!! Player Win!!")
        u_count+=1
        u_w.set(u_count)

    elif u_c == "Rock" and c_c == "Paper":
        res.set("Sorry!! Computer Win!!")
        c_count+=1
        c_w.set(c_count)
    
    elif u_c == "Paper" and c_c == "Scissor":
        res.set("Sorry!! Computer Win!!")
        c_count+=1
        c_w.set(c_count)

    elif u_c == "Scissor" and c_c == "Rock" :
        res.set("Sorry!! Computer Win!!")
        c_count+=1
        c_w.set(c_count)
    
    else:
        res.set("")



l1 = Label(rw,text='Welcome to the Game!!', font=('arial',20,'bold'))
l1.place(x = 150, y= 10)

b1 = Button(rw,text='Rock',width=20,height=2, bg='black',fg='white', command=lambda: c('Rock'))
b1.place(x=50 ,y = 70)

b2 = Button(rw,text='Paper',width=20,height=2,bg='black',fg='white', command=lambda: c('Paper'))
b2.place(x=220,y = 70)

b3 = Button(rw,text='Scissor',width=20,height=2,bg='black',fg='white', command=lambda: c('Scissor'))
b3.place(x=390,y = 70)

l2 = Label(rw,text="User's choice : ",font=('arial',12,'bold')).place(x=50,y=150)
ll2= Label(rw,text="",textvariable=uc ,font=('arial',12,'bold')).place(x=200,y=150)
l3 = Label(rw,text="Computer's choice : ",font=('arial',12,'bold')).place(x=300,y=150)
res1 = Label(rw,text=' ',textvariable=cc ,font=('arial',12,'bold')).place(x=480,y=150)

res1 = Label(rw,text='Result',textvariable=res ,font=('arial',12,'bold')).place(x=200,y=200)
scr = Label(rw,text='Scores :',font=('arial',12,'bold')).place(x=270,y=250)

us = Label(rw,text="User's Win :" ,font=('arial',12,'bold')).place(x=100,y=300)
l1 = Label(rw,text="0", textvariable=u_w,font=('arial',12,'bold')).place(x=140,y=330)


cs = Label(rw,text="Computer's Win :",font=('arial',12,'bold')).place(x=350,y=300)
l1 = Label(rw,text="0", textvariable=c_w,font=('arial',12,'bold')).place(x=400,y=330)

l4 = Label(rw,text='>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<').place(x=10,y=225)
l5 = Label(rw,text='>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<').place(x=10,y=180)

rw.mainloop()