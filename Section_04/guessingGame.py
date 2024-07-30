import random
'''
highest=10
answer = random.randint(1,10) # inclusive 1 to  10 we will get random number 
print(answer) # TODO: Remove after testing 
print("Please guess number between 1 to {}: ".format(highest))
guess=int(input())

if(guess<answer):
    print("Please guess higher")
elif(guess>answer):
    print("Please guess lower")
else:
    print("Hurray!! you guessed it right")
    
'''
# using while loop modify the code 
answer=random.randint(1,10)
print("the random answer is:",answer)
highest=10
while(answer):
    print("Guess the number between 1 to {}: ".format(highest))
    guess=int(input())
    
    if(guess<answer):
        print("Please guess higher")
    elif(guess>answer):
        print("Please guess lower")
    else:
        print("Hurray!! you guessed it right")
        break

