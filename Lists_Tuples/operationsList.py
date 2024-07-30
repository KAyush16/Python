'''
available_parts=["Computers", 
                 "Keyboards", 
                 "Mouse",
                 "Moniter",
                 "HDMI cables", 
                 "DVD drives"
                ]

print(available_parts[2])
del available_parts[1]
print(available_parts)
print(len(available_parts))
'''
data=[4,5,104,105,110,120,130,130,150,
      160,170,183,185,187,191,350,360]

min_valid=100
max_valid=200

# '''enumerate is used to loop through the data list 
# while keeping track of both the index and the value of each element. '''
# for index, value in enumerate(data):
#     if(value<min_valid) or (value>max_valid):
#         del data[index]
        
# print(data)

#process the low values in the list 
stop=0
for index, value in enumerate(data):
    if value>=min_valid:
        stop=index
        break
print(stop) #for debugging
del data[:stop]
print(data)

print(len(data))
#processing the high value in the list 
start=0
# we will process the for loop in the backward direction 
for index in range(len(data)-1,-1,-1): #it will go till 0th index 
    if data[index]<=max_valid:
        start=index+1
        break
print(start)
del data[start:]
print(data)
