import tkinter
tw=tkinter.Tk()
#tw is refference of tkinter class
#title() and mainloop() are instance members of tkinter class hence refference tw can call them
#title() - changes the title of root window
tw.title("My Gui App")
#next 2 lines changes the logo on the screen
img=tkinter.PhotoImage(file="E:/project related/NBA web page/lebron-james-wallpapers.png")
tw.iconphoto(tw,img)
#to the the size of the screen
#geometry("width_x_height")
tw.geometry("600x400")
#to set the position of screen
#geometry("width_x_height+distance_from_left_end+distance_from_top")
tw.geometry("600x400+350+150")
#to make the window appear on the center of the screen...we'll use the maths as screen size as 50% of total size and leaving 25%on all the sides
sw=tw.winfo_screenwidth()
sh=tw.winfo_screenheight()
ww=sw//2
wh=sh//2
x=sw//4
y=sh//4
print(ww)
print(wh)
tw.geometry(f"{ww}x{wh}+{x}+{y}")#f string is used as we need to convert variables to string...variables are written within {} braces
tw.resizable(False,False)
#adding widgets to the screen
lbl1=tkinter.Label(tw,text="Be Cool ... Be Dude")
lbl2=tkinter.Label(tw,text="python rocks!...")
#pack() is necessary to make label appear on the screen
#the order in which we pack resultes in the same order in whick they appear on screen irrespective of order of creating them(lbl1 or lbl2)
lbl1.pack()
lbl2.pack()
tw.mainloop()
#program pauses after mainloop(). the program will move forward only when we'll close the window.
#hence in gui application we will always use mainloop() in the end to display the screen.
