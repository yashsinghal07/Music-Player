from tkinter import *
from tkinter import filedialog,messagebox

def showopenonpopup():
    fname=filedialog.askopenfilename(title="Select your fav song",filetype=[("mp3 files","*.mp3")])
    if fname!="":
        messagebox.showinfo("Song Selected!","you selected \n"+fname)
    else:
        messagebox.showinfo("No Selections!","you did not selected any song")


def showopenonlabel():
    ftuple=filedialog.askopenfilenames(title="Select your fav songs",filetype=[("mp3 files","*.mp3")])
    if len(ftuple)>0:
        str=""
        for songname in ftuple:
            str=str+songname+"\n"
        lbl.config(text=str+"\n")
    else:
        messagebox.showinfo("No Selections!", "you did not selected any song")

root=Tk()
root.geometry("600x500")
btn1=Button(root,text=" Open File (single) (pop up) ",command=showopenonpopup)
btn2=Button(root,text=" Open File (multiple) (label) ",command=showopenonlabel)
lbl=Label(root)

btn1.pack()
btn2.pack()
lbl.pack()
root.mainloop()