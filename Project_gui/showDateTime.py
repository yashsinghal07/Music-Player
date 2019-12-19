import datetime
import tkinter

root=tkinter.Tk()

def greet():
    current = datetime.datetime.now()
    x = current.strftime("%d-%B-%Y %H:%M:%S %p")
    if(lbl1["text"]==""):
        lbl1.config(text=x)
    else:
        lbl1.config(text="")

root.geometry("250x150")

bt1=tkinter.Button(root,text="Click on button to display date and time",command=greet)
lbl1=tkinter.Label(root)

bt1.pack()
lbl1.pack()

root.mainloop()