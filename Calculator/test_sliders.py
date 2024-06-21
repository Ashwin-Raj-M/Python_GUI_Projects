from cProfile import label
from cgitb import text
from tkinter import *
root=Tk()

label=Label(root,text="Hello world!").pack()

vertical=Scale(root,from_=0,to=500,bd=5)
vertical.pack(anchor=E)

horizontal=Scale(root,from_=0,to=500,orient=HORIZONTAL)
horizontal.pack(anchor=S)

def scale():
    Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

btn=Button(root,text="click",command=scale).pack()

root.mainloop()