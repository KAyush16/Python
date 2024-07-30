shopping_list=["milk", "pasta" , "eggs" ,"spam", "bread","rice"]
for i in shopping_list:
    if i=="spam":
        continue
    
    print("Buy: "+i)
    
print("-------------")
shopping_list=["milk", "pasta" , "eggs" ,"spam", "bread","rice"]
for i in shopping_list:
    if i=="spam":
        break
    
    print("Buy: "+i)
    print()
    
   
    #output 
'''
Buy: milk
Buy: pasta
Buy: eggs
Buy: bread
Buy: rice
-------------
Buy: milk
Buy: pasta
Buy: eggs
'''
# break uss particular condition pe indentation ke baad tod deta hai
# continue uss particular consition ko chor ke baki print kar deta hai 

# item to be found 
item_to_find="spam"
# a variable defined named found at initiallize it to none 
found_at=None
'''
# for indexing in range(6)
for index in range(len(shopping_list)):
    if(shopping_list[index]==item_to_find):
        found_at=index 
        break
print("Item found at position {}".format(found_at))
'''

# agar jo element find karna hai wo shopping list mai hai 
if item_to_find in shopping_list:
    found_at=shopping_list.index(item_to_find)

if found_at is not None: #if element present hai then print its position 
    print("Position of the element found is: {}".format(found_at))
else:
    print("{} not found".format(item_to_find))

    


