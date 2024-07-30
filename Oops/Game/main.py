from player import Player

# instance Tim
tim= Player("Tim")

print(tim.name)
print(tim.lives)# Access the lives property -> Calls _get_lives -> Prints 3
tim.lives-=1   # Modify the lives property -> Calls _set_lives with lives = 2
print(tim.lives) # Access the lives property again -> Calls _get_lives -> Prints 2
print(tim)
#This calls tim.__str__().The __str__() method executes and returns 
# the formatted string: "Name: Tim, Lives: 3, Level: 1, Score: 0"

tim._lives=9
print(tim)

tim.level=2
print(tim)

tim.level+=5
print(tim)

tim.score=500
print(tim)