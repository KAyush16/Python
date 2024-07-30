class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
    
def greet(customer):
    print(id(customer))
    customer.name="Nitish"
    print(customer.name)
    print(id(customer))


    
cust=Customer("Ankita")
print(id(cust))

greet(cust.name)   

 