from tkinter import *
from PIL import ImageTk,Image

root = Tk()
insertnum = 0
inp = Entry(root, width=10, borderwidth=5)
inp.grid()
javab = 0
num1 = 0
num2 = 0
opt = ''
root.resizable(False,False)
root.title("Calculator")
def enter():
    global javab
    global num1
    global num2
    global opt

    if num1 == 0 and num2 ==0 and opt == '':
        num1 = inp.get()
        print (num1)
        inp.delete(0, END)
    elif num1 != 0 and opt == '':
        opt = inp.get()
        print (opt)
        inp.delete(0, END)
    elif num1 != 0 and opt != '' and num2 == 0:
        num2 = inp.get()
        print (num2)
        inp.delete(0, END)
    if num1 != 0 and num2 != 0 and opt != "" :
        num1 = int(num1)
        num2 = int(num2)

        if opt == "*":
            javab = num1 * num2
            inp.insert(END, javab)
        elif opt == "/":
            javab = num1 / num2
            inp.insert(END, javab)
        elif opt == "-" or opt == "_":
            javab = num1 - num2
            inp.insert(END, javab)
        elif opt == "+":
            javab = num1 + num2
            inp.insert(END, javab)
        elif opt == "^":
            javab = num1 ** num2
            inp.insert(END,javab)


def insert1():
    inp.insert(END, 1)


def insert2():
    inp.insert(END, 2)


def insert3():
    inp.insert(END, 3)


def insert4():
    inp.insert(END, 4)


def insert5():
    inp.insert(END, 5)


def insert6():
    inp.insert(END, 6)


def insert7():
    inp.insert(END, 7)


def insert8():
    inp.insert(END, 8)


def insert9():
    inp.insert(END, 9)


def insert0():
    inp.insert(END, 0)


def zarb():
    opt = "*"
    inp.insert(END, "*")


def jam():
    opt = "+"
    inp.insert(END, "+")


def taghsim():
    opt = "/"
    inp.insert(END, "/")


def tafrigh():
    opt = "-"
    inp.insert(END, "-")

def clear():
    inp.delete(0,END)
def reset():
    global num1
    global num2
    global opt
    global javab
    num1 = 0
    num2 = 0
    opt = ''
    javab = 0
    inp.delete(0, END)
def butback():
    inp.delete(len(inp.get()) - 1, END)
def power():
    opt = "^"
    inp.insert(END, "^")


but1 = Button(root, text="1", padx=30, pady=20, command=insert1)
but1.grid(row=1, column=0)

but2 = Button(root, text="2", padx=30, pady=20, command=insert2)
but2.grid(row=1, column=1)

but3 = Button(root, text="3", padx=30, pady=20, command=insert3)
but3.grid(row=1, column=2)

but4 = Button(root, text="4", padx=30, pady=20, command=insert4)
but4.grid(row=2, column=0)

but5 = Button(root, text="5", padx=30, pady=20, command=insert5)
but5.grid(row=2, column=1)

but6 = Button(root, text="6", padx=30, pady=20, command=insert6)
but6.grid(row=2, column=2)

but7 = Button(root, text="7", padx=30, pady=20, command=insert7)
but7.grid(row=3, column=0)

but8 = Button(root, text="8", padx=30, pady=20, command=insert8)
but8.grid(row=3, column=1)

but9 = Button(root, text="9", padx=30, pady=20, command=insert9)
but9.grid(row=3, column=2)

but0 = Button(root, text="0", padx=30, pady=20, command=insert0)
but0.grid(row=4, column=1)

butz = Button(root, text="*", padx=30, pady=20, command=zarb)
butz.grid(row=1, column=3)

butj = Button(root, text="+", padx=30, pady=20, command=jam)
butj.grid(row=2, column=3)

buttagh = Button(root, text="/", padx=30, pady=20, command=taghsim)
buttagh.grid(row=3, column=3)

buttaf = Button(root, text="-", padx=30, pady=20, command=tafrigh)
buttaf.grid(row=4, column=3)

bute = Button(root, text="-->", padx=30, pady=20, command=enter)
bute.grid(row=4, column=2)

butclear = Button(root, text="C", padx=30, command=clear)
butclear.grid(row=0, column=2)

butreset = Button(root, text="R", padx=30, command=reset)
butreset.grid(row=0, column=1)

butback = Button(root, text="<--", padx=30,pady=20, command=butback)
butback.grid(row=4, column=0)

butpower = Button(root, text="^" , padx= 30 , command=power)
butpower.grid(column = 3,row = 0)
root.iconbitmap('C:/Users/Lion/Downloads/1.ico')
root.mainloop()
