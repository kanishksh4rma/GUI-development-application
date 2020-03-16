# GUI based form for developers
# created by- @lonewolf-X

from tkinter import *

master = Tk()
count=0
# create enteries
f1=Label(master,text="First name")
f1.grid(row=0)
e1=Entry(master)
e1.grid(row=0,column=1)
f2=Label(master,text="Last name")
f2.grid(row=1)
e2=Entry(master)
e2.grid(row=1,column=1)
vartxt = StringVar()
ls1  = Listbox(master)
# print the results
def printthename():
    global e1
    global count
    global ls1
    txt = e1.get()
    count = count+1
    print('Hello!',txt)
    vartxt.set('You have pressed it %d times'%count)

master.title('@its.kanishk_sharma')
var1 = IntVar()
cb1 = Checkbutton(master,text = 'Male   ',variable = var1)
cb1.grid(row=2,column=1)
label2 = Label(master,textvariable= vartxt)
var2 = IntVar()
cb2 = Checkbutton(master,text = 'Female',variable = var2)
cb2.grid(row=3,column=1)
# insert the index
ls1.insert(1,"C++")
ls1.insert(2,"Python")
ls1.insert(3,"Go lang")
ls1.grid(row=4)
# insert buttons & actions
button1 = Button(master,text = 'Submit',command=printthename,activebackground = 'Grey')
button1.grid(row=5,column=1)
label2.grid(row=6)

master.mainloop()
