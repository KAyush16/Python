from enemy import *

random_monseter =Enemy("Basic Enemy", 12, 1)
print(random_monseter)

random_monseter.take_damage(4)
print(random_monseter)

random_monseter.take_damage(8)
print(random_monseter)

random_monseter.take_damage(9)
print(random_monseter)

# method overloading
ugly_troll=Troll()# This creates a Troll instance with default parameters from the Enemy class (name="enemy", hit_points=0, lives=1).
print("Ugly Troll-{}".format(ugly_troll))

another_troll=Troll("Ug",18,1)#This creates a Troll instance with the specified parameters (name="Ug", hit_points=18, lives=1).
print("Another troll-{}".format(another_troll))

brother=Troll("Urg",23)#This creates a Troll instance with the specified parameters (name="Urg", hit_points=23, lives=1), because lives has a default value of 1.
print(brother)
