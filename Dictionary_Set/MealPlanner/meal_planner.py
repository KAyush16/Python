from contents import pantry,recipes

def add_shopping_item(data: dict, item: str , amount:int)->None:
    """ Add a tuple containing 'item' and 'amount' to the 'data' dict."""
    # certain things might apper two times with this approch of append agar wo ingredient dusre recepie mai use huwa to 
    #data.append((item,amount))

    data[item]=data.setdefault(item,0)+amount
    
    '''
    or 
    if item in data:
        data[item]+=amount
    else:
        data[item]=amount
    '''

# display_dict= { str(index+1) : meal for index , meal in enumerate}
display_dict={}
for index, key in enumerate(recipes):
    display_dict[str(index +1)]=key 
# the above line is adding items of the recepies to the display_dict with index start from '1'
# and key i.e the item (Butter chicken, Chickenand chips, pizza etc )= sting representation of the current index i.e=> str(index+1)
    #print(index,key)
'''
display_dict={
    1. "Butter chicken"
    2. Chicken and chips 
    ......
}
'''
shopping_list={}
while True:
    #display menu of recepies we want to cook 
    print("Please choose your recipe")
    print("--------------------------")
    for key , value in display_dict.items(): # since display_dict is a dictionary so ".item()" is very usefull
        print(f"{key}- {value}")
        
    choice=input(": ")
    
    if choice=="0":
        break
    elif choice in display_dict:
        selected_items=display_dict[choice]
        print(f"you have chosen {selected_items}")
        print("checking ingredients.....")
    # display ingredients of the chosen recepies 
        ingredients = recipes[selected_items]
        print(ingredients)
        # checking ingredients used for the reciepe is there in pantry 
        # if some ingredients are not in the pantry or not necessary quanatity
        for food_items,required_quantity in ingredients.items():
            quantity_in_pantry=pantry.get(food_items,0) # to retrive quantity from the pantry 
            if required_quantity<=quantity_in_pantry:
                print(f"\t{food_items} OK")
            else:
                quantity_to_buy=required_quantity - quantity_in_pantry
                #print(f"\tYou don't have necesary ingredients {food_items}")
                print(f"\tYou need to buy {quantity_to_buy} of {food_items}")
                add_shopping_item(shopping_list,food_items,quantity_to_buy) # adding items that we need to buy 

# printing those food items that we need to buy after the sortage in sorted order 
# for things in shopping_list.items():
#     print(things)

# Printing those food items that we need to buy after the shortage in sorted order
for item, amount in sorted(shopping_list.items()):
    print(item, amount)

'''
 we have in the above code, transformed the data so that the key from "Recipes" become 
 the values in "display_dict".
'''