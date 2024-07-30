from tkinter import *
from PIL import ImageTk,Image
root =Tk()
root.title("Learn to code at Codemy.com")

#for any icon : root.iconbitmap('....')
root.iconbitmap('E:\_Life Pics')
my_img= ImageTk.PhotoImage(Image.open("E:\_Life Pics\old bro .jpg"))
my_label=Label(image=my_img)
my_label.pack()





root.mainloop()