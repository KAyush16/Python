available_parts=["computer",
                 "moniter",
                 "keyboard",
                 "mouse",
                 "mouse mat",
                 "hdmi cable"
                ]

current_choice="-" # currnt choice ko abhi kuch bhi maan liye hain

computer_parts=[] #create empty list 

while current_choice!='0': # taab taak chalega jaab tak '0' na aye 
    if current_choice in "123456":# agar current choice 1,2,3,4,5,6 then below condition will fullfil
        print("Adding {} ".format(current_choice))
        if(current_choice=="1"):
            computer_parts.append("computer")
        elif(current_choice=="2"):
            computer_parts.append("moniter")
        elif(current_choice=="3"):
            computer_parts.append("keyboard")
        elif(current_choice=="4"):
            computer_parts.append("mouse")
        elif(current_choice=="5"):
            computer_parts.append("mouse mat")
        elif(current_choice=="6"):
            computer_parts.append("HDMI cable")
    
    # agar 1,2,3,4,5,6 mai se koi na ho number then ye print hoga 
    # enmurate method 
    else:
        print("Please add options from the list below: ")
        for number,part in enumerate(available_parts):
            print("{0}: {1}".format(number+ 1 , part))
    '''    
    else:
        print("Please add options from the list below: ")
        for part in available_parts:
            print("{0}: {1}".format(available_parts.index(part) + 1 , part))
    '''
    current_choice=input() # again current choice will be checked 
    
print(computer_parts)# print the desired computer parts 



