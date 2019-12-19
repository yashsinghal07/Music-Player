from tkinter import *
from tkinter import colorchooser,messagebox

def showcolorpopup():
    fname=colorchooser.askcolor()
    if fname[0] is None:
        messagebox.showinfo("no color","you did not choose any color...")
    else:
        root.config(bg=fname[1])

root=Tk()
root.geometry("200x200")
btn1=Button(root,text=" Choose color ",command=showcolorpopup)
btn1.pack()
root.mainloop()