from tkinter import *
from tkinter import simpledialog,messagebox

def showopen1():
    name=simpledialog.askstring("enter name","what is your name")
    if name is not None:
        messagebox.showinfo("Welcome"," goodmorning "+name)

def showopen2():
    age=simpledialog.askinteger("enter age","what is your age",minvalue=18,maxvalue=70)
    if age is not None:
        messagebox.showinfo("Welcome"," your age is "+str(age))

root=Tk()
root.geometry("200x200")
btn1=Button(root,text=" open dialog name",command=showopen1)
btn1.pack()
btn2=Button(root,text=" open dialog age ",command=showopen2)
btn2.pack()
root.mainloop()