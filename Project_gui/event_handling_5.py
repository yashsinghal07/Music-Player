from tkinter import *
def changecolor(e):
    root["bg"]="red"
def originalcolor(e):
    root["bg"]=oldcolor
root=Tk()
root.geometry("200x200")
root.bind("<Return>",changecolor)
root.bind("<Escape>",originalcolor)
oldcolor=root["bg"]
root.mainloop()
