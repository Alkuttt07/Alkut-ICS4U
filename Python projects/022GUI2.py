from tkinter import *
w1=Tk()
def f1():
    for i in w1.winfo_children():
        i.destroy()
def f2():
    f1()
    l1=Label(w1,width=10,height=10,background="green")
    l1.grid(row=0,column=0)
    b3=Button(w1,text="back",width=10,height=5,command=f4)
    b3.grid(row=1,column=0)

def f3():
    f1()
    l2=Label(w1,width=10,height=10,background="Yellow")
    l2.grid(row=0,column=0)
    b3=Button(w1,text="back",width=10,height=5,command=f4)
    b3.grid(row=1,column=0)


def f4():
    f1()
    t1=Label(w1,text="Welcome!",width=20,height=5)
    b1=Button(w1,text="color1",width=10,height=5,command=f2)
    b2=Button(w1,text="color2",width=10,height=5,command=f3)
    t1.grid(row=0,column=0)
    b1.grid(row=1,column=0)
    b2.grid(row=2,column=0)

f4()
w1.mainloop()