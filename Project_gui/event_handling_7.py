from tkinter import *
def finish():
    sys.exit(0)
def show():
    x=e1.get()
    y=e2.get()

    e3.config(text=x+" "+y)
   # e3.delete(0,END)
   #e3.insert(0,x+" "+y)
   # e3.insert(0,s.set(textvariable))

root=Tk()
root.geometry("200x200")
l1=Label(root,text="First Name")
l2=Label(root,text="Last Name")
e1=Entry(root)
e2=Entry(root)
s=StringVar
e3=Entry(root,textvariable=s)
l3=Label(root,width=20,anchor=W,font="Arial 10 bold")
b1=Button(root,text="Show",command=show)
b2=Button(root,text="Quit",command=finish)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
l3.grid(row=2,columnspan=2,sticky=W)
e3.grid(row=3,columnspan=2)
b1.grid(row=4,column=0,pady=4)
b2.grid(row=4,column=1,pady=0)
root.mainloop()