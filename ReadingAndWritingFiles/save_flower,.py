data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]


plants_filename="plants.txt"
with open(plants_filename,"w")as plants:
    for plant in data:
        plants.write(plant)

# plant_filename="plants.txt"
# with open(plant_filename,"w")as plants:
#     for plant in data:
#         print(plant,file=plants) # here it automatically goes the nextLine becuse in print statement end="\n"
        
# new_list=[]
# with open(plant_filename)as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
        
# print(new_list)

