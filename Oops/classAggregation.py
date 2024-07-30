class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    
    # new method where we are calling change_address of different class member function
    def edit_profile(self, new_name,new_city,new_pincode,new_state):
        self.name=new_name
        self.address.change_address(new_city,new_pincode,new_state)

class Address:
    def __init__(self,city,pincode,state):
        self.city=city
        self.pincode=pincode
        self.state=state
    def change_address(self,new_city,new_pincode,new_state):
        self.city=new_city
        self.pincode=new_pincode
        self.state=new_state
        
add= Address("Kolkata",700156,"Wb")
cust=Customer("Nitish","Male",add)

# editing the details 
cust.edit_profile("Ayush","Rajiv Chok",110001,"Delhi")
print(cust.address.pincode)