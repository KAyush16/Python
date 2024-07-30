# low+(high-low)/2
# hi-lo game
low=1
high=100
print("Please think a number between {} and {}".format(0,100))
input("Press ENTER to Start")
guesses =1
while low!=high:
    print("\tGuessing in the range of {} and {}".format(low,high))
    guess=low+(high-low)//2
    highLow=input("My guess is {}. Should I guess higher or lower? "
                   "Enter h or l or c if my guess was correct "
                   .format(guess)).casefold()
    
    if highLow=="h":
        #GUess higher. The low end of the range becomes 1 greater than the guess. 
        low=guess+1
        pass
    elif highLow=="l":
        #Guess lower. The high end of the range becomes one less than the guess.
        high=guess-1
        pass
    elif highLow=="c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h , l or c")
    guesses=guesses+1
else:
    print("Your number is {}. I guessed it in {} attempts.".format(low, guesses))