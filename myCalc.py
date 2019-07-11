from tkinter import *
import math

window = Tk()
window.geometry('300x400')
window.title("CALCULATOR")

label1 = Label(window, text="Calculator")
label1.place(relx = 0.5 , rely= 0.0, anchor='n')

expr = StringVar()

entryText = Entry(window,width=35, textvariable = expr)
entryText.place(relx=0.5, y=40, anchor=CENTER)

f1= Frame(window)
f1.place(x=50,y=100,anchor='nw')

expr.set("")
e=""

def Calculate():
    global e
    m = eval(e)
    e = str(m)
    expr.set(str(m))

def press(input):
    global e
    e = e + str(input)
    expr.set(e)

def bkspace():
    global e
    length= len(e)
    e = e[:length-1]
    expr.set(e)

def Exp():
    global e
    r = math.exp(eval(e))
    e = str(r)
    expr.set(str(r))

def log():
    global e
    r = math.log(eval(e))
    e = str(r)
    expr.set(str(r))

def squareRoot():
    global e
    r = math.sqrt(eval(e))
    e= str(r)
    expr.set(str(r))

btCalc = Button(window, text= "Calculate",command=Calculate)
btCalc.place(relx=0.5,rely=0.9, anchor="s")

btPlus = Button(f1, text= "+",width=3,height=1,command=lambda: press("+"))
btSub = Button(f1, text= "-",width=3,height=1,command=lambda: press("-"))
btMulti = Button(f1, text= "*",width=3,height=1,command=lambda: press("*"))
btDiv = Button(f1, text= "/",width=3,height=1,command=lambda: press("/"))
bt1 = Button(f1, text= "1",width=3,height=1,command=lambda: press(1))
bt2 = Button(f1, text= "2",width=3,height=1,command=lambda: press(2))
bt3 = Button(f1, text= "3",width=3,height=1,command=lambda: press(3))
bt4 = Button(f1, text= "4",width=3,height=1,command=lambda: press(4))
bt5 = Button(f1, text= "5",width=3,height=1,command=lambda: press(5))
bt6 = Button(f1, text= "6",width=3,height=1,command=lambda: press(6))
bt7 = Button(f1, text= "7",width=3,height=1,command=lambda: press(7))
bt8 = Button(f1, text= "8",width=3,height=1,command=lambda: press(8))
bt9 = Button(f1, text= "9",width=3,height=1,command=lambda: press(9))
bt0 = Button(f1, text= "0",width=3,height=1,command=lambda: press(0))
btPt = Button(f1, text= ".",width=3,height=1,command=lambda:press("."))
btSqrt = Button(f1, text= "sqrt",width=3,height=1,command=lambda: squareRoot())
btExp = Button(f1, text= "e",width=3,height=1,command=lambda: Exp())
btBkspc =Button(f1, text="DEL",width=3,height=1,command=lambda: bkspace())
btlog =Button(f1, text="log",width=3,height=1,command=lambda: log())
btB1=Button(f1, text="(",width=3,height=1,command=lambda: press("("))
btB2=Button(f1, text=")",width=3,height=1,command=lambda: press(")"))

btExp.grid(row=0,column=0)
btSqrt.grid(row=0,column=1)
btlog.grid(row=0,column=2)
btBkspc.grid(row=0,column=3)
bt1.grid(row=1,column=0)
bt2.grid(row=1,column=1)
bt3.grid(row=1,column=2)
btPlus.grid(row=1,column=3)
bt4.grid(row=2,column=0)
bt5.grid(row=2,column=1)
bt6.grid(row=2,column=2)
btSub.grid(row=2,column=3)
bt7.grid(row=3,column=0)
bt8.grid(row=3,column=1)
bt9.grid(row=3,column=2)
btMulti.grid(row=3,column=3)
btPt.grid(row=4,column=0)
bt0.grid(row=4,column=1)
btB1.grid(row=4,column=2)
btB2.grid(row=4,column=3)


window.mainloop()