'''
class User:
    
    def login(self):
        print("Login")
        
    def register(self):
        print("Register")
        
class Student(User):
    
    def enroll(self):
        print("Enroll")     
    def review(self):
        print("Review")
        
stu1=Student()

stu1.enroll()
stu1.login()
stu1.review()
stu1.register()
'''

################ POlymorphism ################

######## example-1 ############
# method overriding(Polymorphism)
class Phone:
    
    def __init__(self,price,brand,camera):
        print("Inside Phone Constructor!!")
        self.price=price
        self.brand=brand
        self.camera=camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a SmartPhone")
        
s = SmartPhone(20000,"Apple",12)
s.buy()  # this buy will be from the SmartPhone class itself as it alrady contains buy() fn , so no need to inherit from other 

############### example-2 ###############
class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
    
class Child(Parent):
    def __init__(self,val,num):
        self.__val=val
        # solution : super().__init__(num)
        #             self.__val=val
    def get_val(self):
        return self.__val
    
son=Child(100,10)
print("Parent: Num", son.get_num()) 
# error will come as Child has no attribute called" _Parent__num()
print("Child: Val",son.get_val())
 
# since child class has its own Constructors so, Parent constructor is never called, so num was never initialized 

#################### Example-2 ####################
class A:
    def __init__(self):
        self.var1=100
    def display1(self, var1):
        print("Class A",self.var1)
    
class B(A):
    def display2(self, var1): # ham ne parameter: var1 liya but use nahi kiya use kabhi 
        print("Class B",self.var1) # __init__(constructor) wala var1 hai

obj=B()
obj.display1(200)  # outupt: class A: 100
        
############### Super() function ###################
class Parent:
    def __init__(self,num):
        self.__num=num
    def get_num(self):
        return self.__num
    
class Child(Parent):
    def __init__(self,val,num):
        super().__init__(num) # super leyword should always be at the starting of the constructor
        self.__val=val
    def get_val(self):
        return self.__val
    
son=Child(100,10)
print("Parent: Num", son.get_num()) 
print("Child: Val",son.get_val())
 
########### Single Level Inheritance #################
########### Multi-Level Inheritance ##################
########### Hierarchical Inheritance #################
########### Multiple Inheritance  ####################
########### hybrid inheritance ######################