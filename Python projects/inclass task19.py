from tkinter import *
w1=Tk()
a=0

def f1():
    global a
    a+=1
    l1.configure(text=a)
    l1.pack

def f2():
    global a
    a-=1
    l1.configure(text=a)
    l1.pack()
    
l1=Label(master=w1,text=a,foreground="yellow",background="black",width=100,height=20)
b1=Button(master=w1,text="+",foreground="white",background="green",width=100,height=10,command=f1)
b2=Button(master=w1,text="-",foreground="white",background="green",width=100,height=10,command=f2)
l1.pack()
b1.pack()
b2.pack()
w1.mainloop()