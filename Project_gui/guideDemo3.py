import tkinter
tw=tkinter.Tk()
lbl1=tkinter.Label(tw,text="Be Cool ... Be Dude",bg="blue")
lbl2=tkinter.Label(tw,text="Be Cool ",bg="white")
lbl1.pack(fill=tkinter.X,padx=10)
lbl2.pack(fill=tkinter.X,padx=(0,10))
tw.geometry("600x200")
tw.mainloop()