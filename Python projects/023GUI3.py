from tkinter import *
w1=Tk()
t1=Label(w1,text="What's your name?")
e1=Entry(w1)
t2=Label(w1,text="What's the age?")
t4=Label(w1,text="All done.")
t3=Label(w1,text="What's the gender?")

def q2():
    global i1
    i1=e1.get()
    e1.delete(0,END)
    t1.destroy()
    b1.destroy()
    t2.grid(row=0,column=0)
    b2.grid(row=2,column=0)
def q3():
    global i2
    i2=e1.get()
    e1.delete(0,END)
    t2.destroy()
    b2.destroy()
    t3.grid(row=0,column=0)
    b3.grid(row=2,column=0)
def q4():
    global i3
    i3=e1.get()
    e1.destroy()
    t3.destroy()
    b3.destroy()
    t4.grid(row=1,column=0)
    l1=[i1,i2,i3]
    print(l1)
b3=Button(w1,text="Next",command=q4)
b1=Button(w1,text="Next",command=q2)
b2=Button(w1,text="Next",command=q3)
t1.grid(row=0,column=0)
e1.grid(row=1,column=0)
b1.grid(row=2,column=0)
w1.mainloop()