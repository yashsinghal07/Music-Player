import tkinter
root=tkinter.Tk()

root.geometry("195x150")

lbl1=tkinter.Label(root,text="Name: ")
lbl2=tkinter.Label(root,text="Passward: ")

et1=tkinter.Entry(root)
et2=tkinter.Entry(root)

cb1=tkinter.Checkbutton(root,text="keep me logged in")

bt1=tkinter.Button(root,text="Login")
bt2=tkinter.Button(root,text="Exit")

#by default python p;aces elemenst in center of grid tab...to align it we use sticky
#to extend our element across multiple rows and columns we use rowspan and columnspan 
lbl1.grid(row=0,column=0,sticky=tkinter.W)
lbl2.grid(row=1,column=0,sticky=tkinter.W)
et1.grid(row=0,column=1)
et2.grid(row=1,column=1)
cb1.grid(row=2,column=0,columnspan=2,sticky=tkinter.W)
bt1.grid(row=4,column=0)
bt2.grid(row=4,column=1)

root.mainloop()