import tkinter
import tkinter.font as tkfont
tw=tkinter.Tk()
#to change background and foreground of elements such as label
#while making the label
lbl1=tkinter.Label(tw,text="Be Cool ... Be Dude",fg="white",bg="red")
lbl1.pack()
#after craeting the element....use method config() / configure()
lbl2=tkinter.Label(tw,text="yo dude")
#font="<font name single word> <font size> <font style all in lower case>"
lbl2.configure(fg="white",bg="blue",font="Arial 22 bold")
#to pass multiword font name we must pass tuple input as follows
lbl2.configure(font=("Times New Roman",22,"bold"))
#width=30 means width equivalent to 30 charachters atmost
#if we need to chnage only one value then ....
#to apply border borderwidth=2,relief="raised"
#for positioning of the text withim label...anchor="w" all directions"e"/"s"/"n"/"ne"/...
myfont=tkfont.Font(weight="bold")
lbl1.configure(font=myfont,width=30,borderwidth=2,relief="raised",anchor="w")
print(lbl1.keys())
#we can also change atrribute values via dictionary as
lbl2["bg"]="black"
lbl2.pack()
"""img=tkinter.PhotoImage(file="E:/project related/NBA web page/lebron-james-wallpapers.png")
lbl3=tkinter.Label(tw,image=img)
lbl3.pack()"""
msg=tkinter.StringVar()
lbl3=tkinter.Label(tw,textvariable=msg)
msg.set("motherfuckerjones")
lbl3.pack(fill=tkinter.X)
tw.geometry("600x200")
tw.configure(bg="white")
tw.mainloop()