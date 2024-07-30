class Atm:
    #constructor : it calls automatically as the class is called  
    def __init__(self):
        self.pin=""
        self.balance=0
     
        self.menu()# menu method is called here 
    
    def menu(self):
        while(True):
            user_input=input("""
                            Hello, how would you like to proceed?
                            1. Enter 1 to Create Pin
                            2. Enter 2 to Withdraw 
                            3. Enter 3 to Deposit
                            4. Enter 4 to Check Balance 
                            5 Enter 5 to Exit
    """)
        
            if user_input =="1":
                self.create_pin()
            elif user_input=="2":
                self.withdraw()
            elif user_input=="3":
                self.deposit()
            elif user_input=="4":
                self.check_balance()
            elif user_input== "5":
                print("bye")
                break
            else:
                print('Invalid Input, please try again')
                
    def create_pin(self):
        self.pin=input("Enter Your Pin: ")
        print("Pin set Successfully!!")
        
    def deposit(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter the amount to Deposit:"))
            self.balance+=amount
        else:
            print("Invalid Pin!!")
            
    def withdraw(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:
            amount=int(input("Enter the amount to Withdraw:"))
            if amount<self.balance:
                self.balance-=amount
                print("Withdrawn Successful")
            else:
                print("Insufficient Funds!!")
        else:
            print("Invalid Pin!!")
            
    def check_balance(self):
        temp=input("Enter your pin: ")
        if temp==self.pin:    
            print("Your balance is: ",self.balance)
        else:
            print("Invalid Pin!!")    
            
        
sbi=Atm()