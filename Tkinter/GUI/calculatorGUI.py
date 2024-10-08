import tkinter
from tkinter import *
root=Tk()
#title of the Code: Calculator
root.title("Basic Calculator")

#input up my data 
# a box where we will be putting input(Entry of the numbers)
e= Entry(root,width=35,borderwidth=10)
e.grid(row=0,column=0,columnspan=3,padx=20,pady=20) #we have a span of 3 as we will have 3 colums under-neath

#clicking buttons function 
def button_click(number):
    #e.delete(0,END)
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    '''The e.delete(0, END) method does delete all the text temporarily.
    However, immediately after deleting, the e.insert(0, str(current) + str(number)) line 
    insertsthe original text (current) concatenated with the new number.'''

#clicking 'C' it will clear elements 
def button_clean():
    e.delete(0,END)
    
def button_add():
    first_number=e.get()
    global f_num 
    global math
    math="addition"
    f_num=float(first_number)#f_num=float(e.get())
    e.delete(0,END)
    
def button_subtract():
    first_number=e.get()
    global f_num 
    global math
    math="subtraction"
    f_num=float(first_number)
    e.delete(0,END)
    
    
def button_mul():
    first_number=e.get()
    global f_num 
    global math
    math="multiplication"
    f_num=float(first_number)
    e.delete(0,END)
    
    
def button_div():
    first_number=e.get()
    global f_num 
    global math
    math="division"
    f_num=float (first_number)
    e.delete(0,END)

def button_equals():
    second_number=e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,f_num+float(second_number))
    if math=='subtraction':
        e.insert(0,f_num-float(second_number))
    if math=='multiplication':
        e.insert(0,f_num*float(second_number))
    if math=='division':
        e.insert(0,f_num/float(second_number))
    

    
# various keys: at different position: 0-9,various operators 

#define buttons
button_1=Button(root, text='1', padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(1)) # we can use Lambda to pass parameters in buttons 
button_2=Button(root, text='2', padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(2))
button_3=Button(root, text='3', padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(3))
button_4=Button(root, text='4', padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(4))
button_5=Button(root, text='5', padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(5))
button_6=Button(root, text='6', padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(6))
button_7=Button(root, text='7',padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(7))
button_8=Button(root, text='8', padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(8))
button_9=Button(root, text='9', padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(9))
button_0=Button(root, text='0', padx=40, pady=20,fg='black',bg='#D3D3D3', command = lambda:button_click(0))

button_addition=Button(root, text="+", padx=40,pady=20,fg='black',bg='#D3D3D3',command=button_add)
button_subtraction =Button(root, text="-", padx=41,pady=20,fg='black',bg='#D3D3D3',command=button_subtract)
button_multiplication=Button(root, text="*", padx=41,pady=20,fg='black',bg='#D3D3D3',command=button_mul)
button_division=Button(root, text="/", padx=41,pady=20,fg='black',bg='#D3D3D3',command=button_div)

button_clear=Button(root, text="C", padx=90,pady=20,fg='black',bg='#D3D3D3',command=button_clean)
button_equal=Button(root, text="=", padx=89,pady=20,fg='black',bg='#D3D3D3',command=button_equals)

# Position of the buttons on the screen 

button_7.grid(row= 1, column=0)
button_8.grid(row= 1, column=1)
button_9.grid(row=1 , column=2)

button_4.grid(row=2 , column=0)
button_5.grid(row=2 , column=1)
button_6.grid(row=2 , column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row= 4, column=0)

button_addition.grid(row=5,column=0)
button_subtraction.grid(row=6,column=0)
button_multiplication.grid(row=6,column=1)
button_division.grid(row=6,column=2)

button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)


root.mainloop()