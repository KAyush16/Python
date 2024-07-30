class Player:
    def __init__(self, name):
        self.name=name
        self._lives=3
        self._level=1
        self._score=0
    # Lives getter and setter
    def _get_lives(self):
        return self._lives
    def _set_lives(self,lives):
        if lives>=0:
            self._lives=lives
        else:
            print("Lives cannot be negative")
            self._lives=0
    # Levels getter and setter   
    def _get_level(self):
        return self._level
    def _set_level(self,level):
        if level>0:
            delta=level-self._level
            self.score+=delta*1000
            self._level=level
        else:
            print("Level can't be less than 1")
            
    lives=property(_get_lives,_set_lives)
    level=property(_get_level,_set_level)
    
    # score  Decorators
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,score):
        self._score=score
    
    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level:{0._level}, Score: {0.score}".format(self) # or=> format(self.name, self.lives, ....)
    
'''
Infinite Recursion: Using self.lives(insted of self._lives) inside _set_lives calls the setter method again, leading to infinite recursion.
Correct Access: Use the underlying attribute (self._lives) inside getter and setter methods to prevent this issue.
'''


'''
What Happens with lives = property(_get_lives(), _set_lives())
When you write: lives = property(_get_lives(), _set_lives())

You are actually calling _get_lives() and _set_lives() immediately and passing their return values to property. Here’s the step-by-step breakdown of why this is incorrect:

Calling Methods Immediately:

_get_lives() is called immediately when the property line is executed, which will raise an AttributeError because _get_lives is trying to access self._lives, but self is not defined in this context.

_set_lives() is also called immediately, but without the necessary lives argument, which will raise a TypeError.

Expected Callables:
property expects the names of methods (which are callable objects), not the results of calling those methods.
'''