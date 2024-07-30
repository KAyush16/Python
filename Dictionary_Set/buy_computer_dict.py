available_parts={"1": "computer",
                 "2": "moniter",
                 "3": "keyboard",
                 "4": "mouse",
                 "5": "mouse mat",
                 "6": "hdmi cable"
                }

current_choice=None
#computer_parts=[] # creating a list to store the elements 
computer_parts={}
while current_choice !='0':
    if(current_choice in available_parts):
        chosen_part = available_parts[current_choice]
        
        if chosen_part in computer_parts:
            # it's already in the list, so remove it
            print(f"Removing {chosen_part}")
            #computer_parts.remove(chosen_part)
            computer_parts.pop(current_choice)
        else:
            # adding chosen_part in the list 
            print(f"Adding {chosen_part}")
            #computer_parts.append(chosen_part)
            computer_parts[current_choice]=chosen_part
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please add options from the list: ")
        for key,value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")
        
        
    current_choice=input("> ")
