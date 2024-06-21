from cProfile import label
from tkinter import *
root=Tk()
root.geometry("200x100")

def show():
    Label(root,text=drop.get()).pack()

options=[
    "sunday",
    "Monday",
    "Tuesday",
    "Wedneday",
    "Thursday",
    "Friday",
    "Saturday"
]

drop=StringVar()
#To set default values
drop.set(options[0])
#should use "*" in the list call while using list for declaring the dropDown values
dropdown=OptionMenu(root,drop,*options).pack()
btn=Button(root,text="selection",command=show).pack()

#without using list
"""drop=StringVar()
drop.set("Sunday")
dropdown=OptionMenu(root,drop,"sunday","Monday","Tuesday","Wedneday","Thursday","Friday","Saturday").pack()
btn=Button(root,text="selection",command=show).pack()
"""
root.mainloop()