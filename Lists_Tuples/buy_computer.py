current_choice="-"
computer_parts=[]

while current_choice!="0":
    if current_choice in "123456": # agar current choice hai in 12345 then uske agge wla print hoga
        print("Adding {}".format(current_choice))
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
    else:
        print("Please add options from the list Below: ")
        print("1: computer")
        print("2: moniter")
        print("3: keyboard")
        print("4: mouse")
        print("5: mouse mat")
        print("6: HDMI cable")
        print("0: Exit")
        
    current_choice=input()
    
print(computer_parts)


