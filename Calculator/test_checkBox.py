from tkinter import*
root=Tk()
root.geometry("200x100")

def show(state):
    if state==StringVar:
        Label(root,text=str(state)).pack()
    else:    
        Label(root,text=state).pack()

#To show IntVar mode
var1=IntVar()
check1=Checkbutton(root,text="Check me!",variable=var1,command=lambda: show(var1.get())).pack()

#To show StringVar mode
var2=StringVar()
check2=Checkbutton(root,text="Check you!",variable=var2,onvalue="on",offvalue="off",command=lambda: show(var2.get()))
#while using in string mode the box is checked automaticallu so follow this while using StringVar()
check2.deselect()
check2.pack()


root.mainloop()