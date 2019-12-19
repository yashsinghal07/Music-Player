import tkinter
root=tkinter.Tk()

counter=1

def greet():
    global counter
    lbl1.config(text=str(counter))
    counter=counter+1

def greet1():
    obj.set(obj.get()+1)

root.geometry("195x150")

bt1=tkinter.Button(root,text="Click me (global)",command=greet)
lbl1=tkinter.Label(root,text="0")

bt2=tkinter.Button(root,text="Click me (obj)",command=greet1)
obj=tkinter.IntVar()
lbl2=tkinter.Label(root,textvariable=obj)

bt1.pack()
lbl1.pack()
bt2.pack()
lbl2.pack()

root.mainloop()