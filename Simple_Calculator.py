from tkinter import *
root=Tk()
root.geometry("324x490")
root.configure(bg="light blue")
root.title("Calculator")



e=Entry(root,width=32,borderwidth=7,font=20,bg="light green")
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def ButtonClick(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))

def Clear():
    e.delete(0,END)

def add():
    first_number=e.get()
    global fnum
    global fun
    fun="addition"
    fnum=int(first_number)
    e.delete(0,END)

def sub():
    first_number=e.get()
    global fnum
    global fun
    fun="subtraction"
    fnum=int(first_number)
    e.delete(0,END)

def mul():
    first_number = e.get()
    global fnum
    global fun
    fun="multiplication"
    fnum = int(first_number)
    e.delete(0, END)

def div():
    first_number = e.get()
    global fnum
    global fun
    fun="division"
    fnum = int(first_number)
    e.delete(0, END)

def mod():
    first_number = e.get()
    global fnum
    global fun
    fun="modolous"
    fnum = int(first_number)
    e.delete(0, END)



def equal():
    second_number=e.get()
    e.delete(0,END)
    if fun=="addition":
        e.insert(0,fnum+int(second_number))

    if fun=="subtraction":
        e.insert(0,fnum-int(second_number))

    if fun=="multiplication":
        e.insert(0,fnum*int(second_number))

    if fun=="division":
        e.insert(0,fnum/int(second_number))

    if fun=="modolous":
        e.insert(0,fnum%int(second_number))




button1=Button(root,text="1",padx=40,pady=20,font=(20),bg="light green",fg="red",command=lambda:ButtonClick(1))
button2=Button(root,text="2",padx=40,pady=20,font=20,bg="light green",fg="red",command=lambda:ButtonClick(2))
button3=Button(root,text="3",padx=40,pady=20,font=20,bg="light green",fg="red",command=lambda:ButtonClick(3))
button4=Button(root,text="4",padx=40,pady=20,font=20,bg="light green",fg="red",command=lambda:ButtonClick(4))
button5=Button(root,text="5",padx=40,pady=20,font=20,bg="light green",fg="red",command=lambda:ButtonClick(5))
button6=Button(root,text="6",padx=40,pady=20,font=20,bg="light green",fg="red",command=lambda:ButtonClick(6))
button7=Button(root,text="7",padx=40,pady=20,font=20,bg="light green",fg="red",command=lambda:ButtonClick(7))
button8=Button(root,text="8",padx=40,pady=20,font=20,bg="light green",fg="red",command=lambda:ButtonClick(8))
button9=Button(root,text="9",padx=40,pady=20,font=20,bg="light green",fg="red",command=lambda:ButtonClick(9))
button0=Button(root,text="0",padx=40,pady=20,font=20,bg="light green",fg="red",command=lambda:ButtonClick(0))
button00=Button(root,text="Mod",padx=29,pady=20,font=20,bg="light green",fg="red",command=mod)

button_add=Button(root,text="+",padx=40,pady=20,font=20,bg="light green",fg="red",command=add)
button_sub=Button(root,text="-",padx=42,pady=20,font=20,bg="light green",fg="red",command=sub)
button_mul=Button(root,text="x",padx=41,pady=20,font=20,bg="light green",fg="red",command=mul)
button_div=Button(root,text="/",padx=42,pady=20,font=20,bg="light green",fg="red",command=div)
button_equal=Button(root,text="=",padx=94,pady=20,font=20,bg="light green",fg="red",command=equal)
button_clear=Button(root,text="C",padx=42,pady=22,bg="light green",fg="red",command=Clear)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=2)
button00.grid(row=5,column=2)
button_add.grid(row=4,column=0)
button_sub.grid(row=5,column=0)
button_mul.grid(row=5,column=1)
button_div.grid(row=4,column=1)
button_equal.grid(row=6,column=1,columnspan=3)
button_clear.grid(row=6,column=0)


root.mainloop()