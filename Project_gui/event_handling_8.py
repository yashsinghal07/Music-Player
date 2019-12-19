from tkinter import *
from tkinter import messagebox
root = Tk()
def divide():
    try:
        e3.delete(0,END)
        x=int(e1.get())
        y=int(e2.get())
        e3.insert(0,x/y)
        e3.config(fg="green")
    except ZeroDivisionError:
        #e3.insert(0,"Divide By 0!")
        #e3.config(fg="red")
        messagebox.showerror("Arithmatic error!","Denominator shoud be positive...")
    except ValueError:
        #e3.insert(0,"Only digits allowed")
        #e3.config(fg="red")
        messagebox.showerror("Wrong input!", "Only digits allowed...")

def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.focus()
def finish():
    #root.destroy()
    answer=messagebox.askyesno("quitting","do you really want to quit!")
    if(answer==True):
        root.destroy()
root.geometry('400x200+100+200')
l1=Label(root, text="Number Division Program",font="Arial 18 bold")
l2=Label(root, text="First No:")
l3=Label(root, text="Second No:")
l4=Label(root,text="Result:")
e1=Entry(root)
e2=Entry(root)
e3=Entry(root)
b1=Button(root,text="Divide",command=divide)
b2=Button(root,text="Clear",command=clear)
b3=Button(root,text="Quit",command=finish)
l1.grid(row=0,column=0,columnspan=4)
l2.grid(row=1,column=0,sticky=E)
e1.grid(row=1,column=1)
l3.grid(row=2,column=0,sticky=E)
e2.grid(row=2,column=1)
l4.grid(row=3,column=0,sticky=E)
e3.grid(row=3,column=1)
b1.grid(row=4,column=0,pady=5,padx=5,sticky=E+W)
b2.grid(row=4,column=1,pady=5,padx=5,sticky=E+W)
b3.grid(row=4,column=2,pady=5,padx=5,sticky=E+W)
root.mainloop()
