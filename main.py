# GUI based registration form for developer
# created by- @lonewolf-X
# instagram - @its.kanishk_sharma

from tkinter import *
from datetime import date
import time

master = Tk()
count=0
# create enteries
f1=Label(master,text="First name")      
f1.grid(row=0)
e1=Entry(master)                 #to create entry box for first name
e1.grid(row=0,column=1)
f2=Label(master,text="Last name")
f2.grid(row=1)
e2=Entry(master)                 #to create entry box for last name
e2.grid(row=1,column=1)
f3=Label(master,text="Address")
f3.grid(row=2)
e3=Entry(master)                 #to create entry box for address
e3.grid(row=2,column=1)
vartxt = StringVar()             #to store a string whose value isn't constant
ls1  = Listbox(master)

#for pop-up msg
def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()
    
# print the results
def printthename():
    global e1
    global count
    global ls1
    global file1
    global flag
    global var1,var2
    n1 = str(e1.get())
    n2 = e2.get()
    add = e3.get()
    ch1=str((ls1.get(ACTIVE)))
    gen1=int(var1.get())
    gen2=''
    flag=1
    if e1.get() == '':
    	flag=0
    	print('WARNING : Name can\'t be empty !!')
    if gen1 == 1 and var2.get() == 1:
    	var1.set(0)
    	var2.set(0)
    	print('WARNING : two genders can\'t be possible')
    	flag=0
    if flag==0:
    	
    	print('Registration Aborted!!')
    	exit(0)


    if gen1==1:
    	gen2='Male'
    else:
    	gen2='Female'
    count = count+1
    print('Registration Successfull!!')
    # file insertion

    file1.write('\nName : %s'%str(n1+' '+n2))
    file1.write('\nAddress : %s'%str(add))
    file1.write('\nGender : %s'%gen2)
    file1.write('\nLanguage : %s'%ch1)
    msg = "Form for %s is successfully submitted !!"%n1
    alert_popup("Success!", "Processing completed Successfully!!. ",msg)



master.title('@its.kanishk_sharma')             #title of the GUI-window
var1 = IntVar()
cb1 = Checkbutton(master,text = 'Male   ',variable = var1)  #to create check box-1
cb1.grid(row=3,column=1)
label2 = Label(master,textvariable= vartxt)
var2 = IntVar()
cb2 = Checkbutton(master,text = 'Female',variable = var2)   #to create check box-2
cb2.grid(row=4,column=1)
# insert the index
flag=1
ls1.insert(1,"C++")                             
ls1.insert(2,"Python")
ls1.insert(3,"Go lang")
ls1.grid(row=5)

# insert buttons & actions
file1 = open("form.txt","a")
button1 = Button(master,text = 'Submit',command=printthename,activebackground = 'Grey')
if flag==1:
	d = date.today()					# to access date & time
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)

	file1.write('\nRegistration time : %s'%(str(d)))
	file1.write(' %s'%(str(current_time)))
	file1.write('\n===========================================')

button1.grid(row=6,column=1)
label2.grid(row=7)
#master.mainloop() 
file1.close()
