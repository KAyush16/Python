vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# adding items in dictionary(it gets added to the end if we not specify)
vehicles["starfighter"]="Lockhead F-104"

# updating values in Dictionary
vehicles['virago']="ayush"

# removing items in dictionary 
del vehicles['virago']
# printing key of the dictionary
new_vehicle=vehicles['can-am']
print(new_vehicle)
print()

# iterating over the dictionary
for key,value in vehicles.items():
    #print(key,vehicles[key],sep=", ")
    print(f"{key}: {value}")
    #or print(key,value,sep=", ")
    
# deleting over the dictionary 

