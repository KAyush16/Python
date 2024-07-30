from packingList_sets import*
mode = "-"
while mode not in travel_mode:
    mode = input("> ")

if mode == "2":
    # travelling by plane, remove restricted items
    pass

# print the packing list
print("You need to pack:")
for item in sorted(items):
    print(item)