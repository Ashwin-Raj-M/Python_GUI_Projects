from msilib.schema import RadioButton
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import ttk
root=Tk()
food=StringVar()
food.set("Burger")

def clicked(value):
    mylable=Label(root,text=value).pack()
items=[
    ("burger","Burger"),
    ("pizza","Pizza"),
    ("macroons","Macroons"),
    ("twinkies","Twinkies"),
]
for text,mode in items:
    Radiobutton(root,text=text,variable=food,value=mode).pack(anchor=W)

button=ttk.Button(root,text="button",command=lambda: clicked(food.get())).pack()
root.mainloop()