import tkinter
tw=tkinter.Tk()
lbl1=tkinter.Label(tw,text="Be Cool ... Be Dude",bg="blue")
lbl2=tkinter.Label(tw,text="Be Cool ",bg="white")
lbl1.grid(row=0,column=0)
lbl2.grid(row=1,column=1)
tw.geometry("600x200")
tw.mainloop()