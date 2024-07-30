available_exit=["north", "south","east","west"]
chosen_exit=""
while chosen_exit not in available_exit:
    chosen_exit=input("Please choose the direction:")
    if chosen_exit.casefold()=="quit":
        print("Game Over")
        break
    else:
        print("aren't you glad you got there!! ")
        
