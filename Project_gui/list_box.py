from tkinter import *
from tkinter import simpledialog,messagebox

def show():
    pos=lbl.curselection()
    if(len(pos)==0):
        messagebox.showerror("NO Selection","please select atleast one of them")
    else:
        sname=lbl.get(pos[0])
        lbl1.config(text="you selected "+sname)
root=Tk()
root.geometry("300x300")
lbl=Listbox(root)
sports=["cricket","football","basketball","kanchey"]
#pos=0
for s in sports:
    #lbl.insert(pos,s)
    #pos+=1
    lbl.insert(END,s)
lbl.grid(row=1,column=0,sticky=W)

btn1=Button(root,text=" Choose game ",command=show)
btn1.grid(row=2,column=0,sticky=W)
lbl1=Label(root)
lbl1.grid(row=3,column=0,sticky=W)
root.mainloop()

# lbl.delete(first,last=none)
# lbl.size()