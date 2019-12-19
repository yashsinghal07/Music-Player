import tkinter
import datetime
root=tkinter.Tk()

def greet():
    if(lbl1["text"]==""):
        lbl1.config(text="welcome to python")
    else:
        lbl1.config(text="")

root.geometry("195x150")

bt1=tkinter.Button(root,text="Click me",command=greet)
lbl1=tkinter.Label(root)

bt1.pack()
lbl1.pack()

root.mainloop()