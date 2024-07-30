import tkinter

mainWindow=tkinter.Tk()

mainWindow.title("Hellow Window") 
mainWindow.geometry('640x480+8+480')


label=tkinter.Label(mainWindow,text="Hello World")
label.pack(side="top")

leftFrame=tkinter.Frame(mainWindow)
leftFrame.pack(side="left",anchor='n',fill=tkinter.Y,expand=False)
# the canvas design have been put in the left frame 
canvas=tkinter.Canvas(leftFrame,relief='raised',borderwidth=1)
canvas.pack(side='left',anchor='n')

#the buttons have been put in the right frame 

rightFrame=tkinter.Frame(mainWindow)
rightFrame.pack(side='right',anchor='n',expand=True)

#canvas=tkinter.Canvas(mainWindow,relief='raised',borderwidth=1)
#cavas.pack(side='top',fill=tkinter.X,expand=True) 

button1=tkinter.Button(rightFrame,text='Button1')
button2=tkinter.Button(rightFrame,text='Button2')
button3=tkinter.Button(rightFrame,text='Button3')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')

mainWindow.mainloop()

 



