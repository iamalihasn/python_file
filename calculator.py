from tkinter import*

window = Tk()
window.geometry("500x500")
window.title("Calculator")

#Calculator screen

e = Entry(
    window,
    width=43,
    borderwidth=10,
    bg="#a2bbcf",
    justify="right"
)
e.place(x=0,y=0)


# click method

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,result+str(num))


# buttons(Operands) of Calculator

btn1 = Button(window,text="1",width=10,bg="black",fg="white",command=lambda:click(1))
btn1.place(x=10,y=60)


btn2 = Button(window,text="2",width=10,bg="black",fg="white",command=lambda:click(2))
btn2.place(x=100,y=60)


btn3 = Button(window,text="3",width=10,bg="black",fg="white",command=lambda:click(3))
btn3.place(x=190,y=60)


btn4 = Button(window,text="4",width=10,bg="black",fg="white",command=lambda:click(4))
btn4.place(x=10,y=90)


btn5 = Button(window,text="5",width=10,bg="black",fg="white",command=lambda:click(5))
btn5.place(x=100,y=90)


btn6 = Button(window,text="6",width=10,bg="black",fg="white",command=lambda:click(6))
btn6.place(x=190,y=90)


btn7 = Button(window,text="7",width=10,bg="black",fg="white",command=lambda:click(7))
btn7.place(x=10,y=120)


btn8 = Button(window,text="8",width=10,bg="black",fg="white",command=lambda:click(8))
btn8.place(x=100,y=120)


btn9 = Button(window,text="9",width=10,bg="black",fg="white",command=lambda:click(9))
btn9.place(x=190,y=120)


btn0 = Button(window,text="0",width=10,bg="black",fg="white",command=lambda:click(0))
btn0.place(x=10,y=150)

# operator buttons and function

def add():
    n1 = e.get()
    global operator
    operator = "addition"
    global i
    i = int(n1)
    e.delete(0,END)


btn0 = Button(window,text="+",width=10,bg="black",fg="white",command=add)
btn0.place(x=100,y=150)

def sub():
    n1 = e.get()
    global operator
    operator = "subtract"
    global i
    i = int(n1)
    e.delete(0,END)


btn0 = Button(window,text="-",width=10,bg="black",fg="white",command=sub)
btn0.place(x=190,y=150)


def product():
    n1 = e.get()
    global operator
    operator = "multiplication"
    global i
    i = int(n1)
    e.delete(0,END)

btn0 = Button(window,text="*",width=10,bg="black",fg="white",command=product)
btn0.place(x=10,y=180)

def div():
    n1 = e.get()
    global operator
    operator = "division"
    global i
    i = int(n1)
    e.delete(0,END)


btn0 = Button(window,text="/",width=10,bg="black",fg="white",command=div)
btn0.place(x=100,y=180)

def equal():
    n2 = e.get()
    e.delete(0,END)

    if operator == "addition":
        e.insert(0,i+int(n2))

    elif operator == "subtract":
        e.insert(0,i-int(n2))

    elif operator == "multiplication":
        e.insert(0,i*int(n2))

    elif operator == "division":
        e.insert(0,i/int(n2))


btn0 = Button(window,text="=",width=36,bg="black",fg="white",command=equal)
btn0.place(x=10,y=210)


def clear():
    e.delete(0,END)

btn0 = Button(window,text="Clear",width=10,bg="red",fg="white",command=clear)
btn0.place(x=190,y=180)




window.mainloop()