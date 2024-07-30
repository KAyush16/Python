'''
import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)
# tkinter.TkVersion: This prints the version of Tk (the GUI toolkit used by tkinter).
# tkinter.TclVersion: This prints the version of Tcl (Tool Command Language), 
# which is used by Tk for scripting




tkinter._test()
#This(_test()) command runs a simple test of the tkinter installation by opening a small window with a "Quit" button.
# This verifies that tkinter is properly installed and working.


mainWindow=tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry('640x480+8+300')
lable=tkinter.Label(mainWindow,text="Hi my name is Ayush")
lable.pack()
mainWindow.mainloop()
'''
from tkinter import *

root = Tk()
root.title("Hi")
# label of the page 
myLabel=Label(root,text="Hello World",borderwidth=4)
myLabel.pack(side='top')

#iput fields 
e=Entry(root,width=50)
e.pack()
e.insert(0,"Enter your name: ")

def myClick():
    myLabel1 = Label(root,text="Hello " +e.get())
    myLabel1.pack()
    

my_Button=Button(root,text="your name is",command=myClick)
my_Button.pack()

root.mainloop()