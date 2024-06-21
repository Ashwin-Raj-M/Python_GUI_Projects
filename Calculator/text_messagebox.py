from struct import pack
from tkinter import *
from tkinter import messagebox
import tkinter
root=Tk()

def popup():
    responce=tkinter.messagebox.askokcancel("message","Are you above 18 ?")
    
    """if responce==1:
        Label(root,text="Your are eligible for vote..").pack()
    else:
        Label(root,text="Your are not eligible for vote..").pack()
    """
    Label(root,text=responce).pack()
button=Button(root,text="popup!",command=popup).pack()
root.mainloop()
"""
types of message boxes: 
    showinfo()
    showwarning()
    showerror()
    askquestion()
    askokcancel()
    askyesno()
"""