from tkinter import *
def changetored(e):
    root.config(bg="red")
def changetogreen(e):
    root.config(bg="green")

root=Tk()
root.geometry("200x200")
b1=Button(root,text="Click me")
b1.pack()
b1.bind("<Button-1>",changetored)
b1.bind("<Button-2>",changetogreen)
root.mainloop()