import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
root=Tk()


def window ():
    top=Toplevel()
    top.iconbitmap("THS_logo_full.ico")
    my=Label(top,text=("Hellow world!")).pack()
    but=Button(top,text="close",command=top.destroy).pack()
    myimg=ImageTk.PhotoImage(Image.open("D:\coding\python\gui\—Pngtree—instagram icon instagram logo_3584852.png"))

but=Button(root,text="click to open new window.",command=window).pack()


root.mainloop()