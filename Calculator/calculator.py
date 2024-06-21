from tkinter import *
root = Tk()
root.title("Calculator")
root.iconbitmap('/media/ashwin23/668B-14EA/coding/python/gui/calculator-icon_34473.ico')
opp=0

# functions

def number(num):
    current = dis.get()
    dis.delete(0, END)
    dis.insert(0, current+str(num))


def add():
    global opp
    opp = 1
    global current1
    current1 = int(dis.get())
    dis.delete(0, END)


def sub():
    global opp
    opp = 2
    global current2
    current2 = int(dis.get())
    dis.delete(0, END)


def mult():
    global opp
    opp = 3
    global current3
    current3 = int(dis.get())
    dis.delete(0, END)


def div():
    global opp
    opp = 4
    global current4
    current4 = int(dis.get())
    dis.delete(0, END)


def equ():
    eq = int(dis.get())
    dis.delete(0, END)
    if opp == 1:
        equ1 = current1+eq
        dis.insert(0, equ1)
    if opp == 2:
        equ2 = current2-eq
        dis.insert(0, equ2)
    if opp == 3:
        equ3 = current3*eq
        dis.insert(0, equ3)
    if opp == 4:
        equ4 = current4/eq
        dis.insert(0, equ4)


def clear():
    dis.delete(0, END)


# display
dis = Entry(root, bd=5, width=50)
dis.grid(column=0, row=0, columnspan=3)

# buttons
button1 = Button(root, text="1", padx=45, pady=20,
                 command=lambda: number(1)).grid(column=0, row=4)
button2 = Button(root, text="2", padx=45, pady=20,
                 command=lambda: number(2)).grid(column=1, row=4)
button3 = Button(root, text="3", padx=45, pady=20,
                 command=lambda: number(3)).grid(column=2, row=4)

button4 = Button(root, text="4", padx=45, pady=20,
                 command=lambda: number(4)).grid(column=0, row=3)
button5 = Button(root, text="5", padx=45, pady=20,
                 command=lambda: number(5)).grid(column=1, row=3)
button6 = Button(root, text="6", padx=45, pady=20,
                 command=lambda: number(6)).grid(column=2, row=3)

button7 = Button(root, text="7", padx=45, pady=20,
                 command=lambda: number(7)).grid(column=0, row=2)
button8 = Button(root, text="8", padx=45, pady=20,
                 command=lambda: number(8)).grid(column=1, row=2)
button9 = Button(root, text="9", padx=45, pady=20,
                 command=lambda: number(9)).grid(column=2, row=2)

button0 = Button(root, text="0", padx=45, pady=20,
                 command=lambda: number(0)).grid(column=0, row=5)
buttonAdd = Button(root, text="+", padx=44, pady=20,
                   command=add).grid(column=1, row=5)
buttonSub = Button(root, text="-", padx=45.4, pady=20,
                   command=sub).grid(column=2, row=5)

buttonMult = Button(root, text="*", padx=45.49, pady=20,
                    command=mult).grid(column=0, row=6)
buttonDiv = Button(root, text="/", padx=45.5, pady=20,
                   command=div).grid(column=1, row=6)
buttonEqu = Button(root, text="=", padx=43, pady=20,
                   command=equ).grid(column=2, row=6)

buttonClear = Button(root, text="Clear", padx=140, pady=20,
                     command=clear).grid(columnspan=3, row=7)
root.mainloop()