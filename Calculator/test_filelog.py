from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

root=Tk()

root.filename=filedialog.askopenfile(initialdir="/gui",text="select a file",filetypes=(("open jpg","*.jpg")))

root.mainloop()