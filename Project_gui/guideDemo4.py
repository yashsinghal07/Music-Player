import tkinter
tw=tkinter.Tk()
lbl1=tkinter.Label(tw,text="Be Cool ... Be Dude",bg="blue")
lbl2=tkinter.Label(tw,text="Be Cool ",bg="white")
lbl1.place(x=0,y=0)
lbl2.place(x=50,y=40)
tw.geometry("600x200")
tw.mainloop()