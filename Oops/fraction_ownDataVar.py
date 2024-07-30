class Fraction:
    def __init__(self,n , d):
        self.num=n
        self.den=d
    
    # magic methods: are called automatically 
    # will show the fraction of two numbers 
    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    
    # for addition(+) its magic method is: __add__
    def __add__(self,other): # here x will go to self and y will go to other(and each will have its own numerator and denominator)
        temp_num=self.num*other.den + self.den*other.num
        temp_den=self.den*other.den
        
        return "{}/{}".format(temp_num,temp_den)
    
    # for subtraction(-) its magic method is: __sub__
    def __sub__(self,other):
        temp_num=self.num*other.den - self.den*other.num
        temp_den=self.den*other.den
        
        simp =f"{temp_num}/{temp_den}"
        return simp
        #return "{}/{}".format(temp_num,temp_den)
        
    # for multiplication(*) its magic method is: __mul__
    def __mul__(self,other):
        temp_num=self.num*other.num
        temp_den=self.den*other.den

        return "{}/{}".format(temp_num,temp_den)
     
    # for division(/) its magic method is: __truediv__
    def __truediv__(self,other):
        temp_num=self.num*other.den
        temp_den=self.den*other.num
        
        return "{}/{}".format(temp_num,temp_den)
     
    
x=Fraction(4,5)
print(x) # it will automaticlly go to the __str__ function 
y=Fraction(6,7)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)