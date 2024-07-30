# global keyword 
def globalVar():
	
	#this will make x global variable so even this x will be created in a function despite it 
    #should ve #local variable it will be accessed everywhere in the code as it has now become the global variable 
    global y 
    y = "Maza"
    print("I like", y,"juice very much")
 
globalVar()


print("The Value of x is:", y)
    