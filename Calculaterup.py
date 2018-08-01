from tkinter import *
from distutils import command
from webbrowser import Opera
from _ast import operator






root= Tk()
root.title('CALCULATOR')

textin=StringVar()
operator=''

def clickbut(numbers):
    global operator
    operator+=str(numbers)
    textin.set(operator)


def eqbut():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=''
# val=StringVar()

def eqbut():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator=''

def eqbut():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator=''
def sq(Event):
    
    x=float(textin.get())
    sq = x*x
    textin.set(sq)
    
def sqrt(Event):
    x=float(textin.get())
    sqrt = x**0.5
    textin.set(sqrt)    

   
    
def clrbut():
    global operator
    textin.set('')
    operator=''
    
    
root.configure(bg='#636363')    
e=Entry(root,textvar=textin,bd=7)
e.grid(row=0,columnspan=9,ipadx=10,pady=10)


but1 = Button(root,text='7',width=5,height=2,command=lambda:clickbut(7),bg='#7cfc00',fg='black',bd=5)
but1.grid(row=1,column=1)

but2 = Button(root,text='8',width=5,height=2,command=lambda:clickbut(8),bg='#7cfc00',fg='black',bd=5)
but2.grid(row=1,column=2)

but3 = Button(root,text='9',width=5,height=2,command=lambda:clickbut(9),bg='#7cfc00',fg='black',bd=5)
but3.grid(row=1,column=3)

butmul = Button(root,text='x',width=5,height=2,command=lambda:clickbut('*'),bg='#7cfc00',fg='black',bd=5)
butmul.grid(row=1,column=4)


but4 = Button(root,text='4',width=5,height=2,command=lambda:clickbut(4),bg='#7cfc00',fg='black',bd=5)
but4.grid(row=2,column=1)


but5 = Button(root,text='5',width=5,height=2,command=lambda:clickbut(5),bg='#7cfc00',fg='black',bd=5)
but5.grid(row=2,column=2)

but6 = Button(root,text='6',width=5,height=2,command=lambda:clickbut(6),bg='#7cfc00',fg='black',bd=5)
but6.grid(row=2,column=3)

butdiv = Button(root,text='/',width=5,height=2,command=lambda:clickbut('/'),bg='#7cfc00',fg='black',bd=5)
butdiv.grid(row=2,column=4)

but7 = Button(root,text='1',width=5,height=2,command=lambda:clickbut(1),bg='#7cfc00',fg='black',bd=5)
but7.grid(row=3,column=1)


but8 = Button(root,text='2',width=5,height=2,command=lambda:clickbut(2),bg='#7cfc00',fg='black',bd=5)
but8.grid(row=3,column=2)

but9 = Button(root,text='3',width=5,height=2,command=lambda:clickbut(3),bg='#7cfc00',fg='black',bd=5)
but9.grid(row=3,column=3)

butadd = Button(root,text='+',width=5,height=2,command=lambda:clickbut('+'),bg='#7cfc00',fg='black',bd=5)
butadd.grid(row=3,column=4)

but0 = Button(root,text='0',width=5,height=2,command=lambda:clickbut(0),bg='#7cfc00',fg='black',bd=5)
but0.grid(row=4,column=1)


butdot = Button(root,text='.',width=5,height=2,command=lambda:clickbut('.'),bg='#7cfc00',fg='black',bd=5)
butdot.grid(row=4,column=2)

butmodu = Button(root,text='%',width=5,height=2,command=lambda:clickbut('%'),bg='#7cfc00',fg='black',bd=5)
butmodu.grid(row=4,column=3)

butsub = Button(root,text='-',width=5,height=2,command=lambda:clickbut('-'),bg='#7cfc00',fg='black',bd=5)
butsub.grid(row=4,column=4)

butac = Button(root,text='AC',width=5,height=2,command=clrbut,bg='#7cfc00',fg='black',bd=5)
butac.grid(row=1,column=8)

butb = Button(root,text='(',width=5,height=2,command=lambda:clickbut('('),bg='#7cfc00',fg='black',bd=5)
butb.grid(row=2,column=8)

butr = Button(root,text='\/',width=5,height=2,bg='#7cfc00',fg='black',bd=5)
butr.grid(row=3,column=8)
butr.bind("<Button-1>", sqrt)
butr.bind("<Return>",sqrt)

butc = Button(root,text='C',width=5,height=2,bg='#7cfc00',fg='black',bd=5)
butc.grid(row=1,column=9)

butb2 = Button(root,text=')',width=5,height=2,command=lambda:clickbut(')'),bg='#7cfc00',fg='black',bd=5)
butb2.grid(row=2,column=9)

butsq = Button(root,text='x^2',width=5,height=2,bg='#7cfc00',fg='#68228b',bd=5)
butsq.grid(row=3,column=9)
butsq.bind("<Button-1>", sq)
butsq.bind("<Return>",sq)

buteq = Button(root,text='=',width=13,height=2,command=eqbut,bg='#7cfc00',fg='black',bd=5)
buteq.grid(row=4,column=8,columnspan=2)


root.mainloop()

