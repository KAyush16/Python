class Kettle(object):
    
    def __init__(self, make ,price):
        self.make=make
        self.price=price
        self.on=False
        
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model   
    def full_name(self):
        return f"{self.brand} {self.model}"
    
 # creat a class ElectricCar that inherits from the Car and has an additional attribute 
class ElectricCar(Car):
    def __init__(self,brand , model , batterySize):
        super().__init__(brand,model)
        self.batterySize=batterySize

        
my_tesla=ElectricCar("tesla","model-s","85kwh")
print(my_tesla.full_name())
 # ************************************ #
kenwood=Kettle("Kenwood",8.99)
print(kenwood.make)    
print(kenwood.price)

kenwood.price=12.65
print(kenwood.price)

hamilton= Kettle("Hamilton",15.24)

print("Models: {} = {} , {} = {} ".format(kenwood.make,kenwood.price,hamilton.make,hamilton.price))

# ********************************************* #
my_car=Car("Toyota","Corolla")
print(my_car.model)
print(my_car.brand)

'''
# here 

Car: is the Class Name 
brand & model: attributes/variable of the class Car and member function __init__

__init__() method is a special method in Python classes that is automatically called when an object of
the class is created. It is used to initialize the attributes of the object.
'''
 
