import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.now()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance # private attribute
        self._transaction_list = [(Account._current_time(), balance)] #Initializes the transaction list with the (current time,opening balance).
        print("Account created for " + self._name) #Prints a message indicating that the account has been created.
        #self.show_balance() # show_balance method is called 

# Depositing the money only if amount>0 and printing the time it was deposited with the amount and adding up in __balance attribute
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))

# Withdrawing the money 0<amount<self.__balance and printing time it was withdrawn with the amount and deducting it from __balance attribute 
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    # class method to print the Available Balance 
    def show_balance(self):
        print("Balance is {}".format(self.__balance))


    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))
            # field width of amount is set to '6' , 

if __name__ == '__main__': # Ensures the following code runs only if the script is executed directly.

    # object/ instance of a class 1
    tim = Account("Tim", 0)#Creates a new Account object for "Tim" with an initial balance of 0.
    tim.show_balance() # initial balance = 0

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()

    tim.withdraw(2000)

    tim.show_transactions()

    # object 2
    steph = Account("Steph", 800)
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    steph.show_balance()
    print(steph.__dict__)
    steph._Account__balance = 40
    steph.show_balance()
