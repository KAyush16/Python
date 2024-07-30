import math
import tkinter

def parabola(page,size):
    for x in range(-size,size):
        y=x*x/size
        plot(page,x,y)

def draw_axis(canvas):
    canvas.update()
    x_origin=canvas.winfo_width() / 2
    y_origin=canvas.winfo_height() /2
    #this line will configure a region of x and y 
    canvas.configure(scrollregion=(-x_origin,-y_origin,x_origin,y_origin))
    # this will create a 'x-axis' and fill with colour= black and with 'y=0'
    canvas.create_line(-x_origin,0,x_origin,0,fill='black')
    # this will create a 'y-axis' and fill with colour= black and with 'x=0'
    canvas.create_line(0,-y_origin,0,y_origin,fill='black')

# plotting the x,y in the graph 
def  plot(canvas,x,y):
    canvas.create_line(x,-y,x+1,- y+1,fill="red")
    #x,-y,x+1,y+1


# circle
def circle(page,radius,g,h,colour="red"):
    page.create_oval(g+radius,h+radius,g-radius,h-radius, outline=colour, width=2)
        
        
mainWindow=tkinter.Tk()
mainWindow.title("Parabola")
mainWindow.geometry("640x480")

canvas=tkinter.Canvas(mainWindow,width=640,height=480)
canvas.grid(row=0,column=0)

draw_axis(canvas)

# # for x in range():
#     y=parabola(canvas,100)
#     plot(canvas,x,y)
#     plot(canvas,y,x)
    
parabola(canvas,100)
parabola(canvas,200)

circle(canvas,100,100,100,"green")
circle(canvas,100,100,-100,"yellow")
circle(canvas,100,-100,100,"black")

mainWindow.mainloop()
