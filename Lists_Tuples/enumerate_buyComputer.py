'''
for index, character in enumerate("abcdefgh"):
    print("{0}: {1}".format(index,character))
'''
# given available parts 
available_parts=["Computers", 
                 "Keyboards", 
                 "Mouse",
                 "Moniter",
                 "HDMI cables", 
                 "DVD drives"
                ]


valid_choice=[] #valid choices ko null rakha hai 

for i in range(1, len(available_parts)+1):
    valid_choice.append(str(i))
print(valid_choice)


current_choices="-"
computer_parts=[] # create empty list
while current_choices!='0':
    if current_choices in valid_choice:
        index=int(current_choices)-1
        chosen_part=available_parts[index]
        
        if chosen_part in computer_parts:
            print("Removing {}".format(chosen_part))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choices))
            computer_parts.append(chosen_part)
            
        print("your list now contains: {}".format(computer_parts))
        
    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number+1,part))
    
    current_choices=input()
print(computer_parts)            

