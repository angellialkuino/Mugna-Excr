
class BankAccount (object):
    interest_rate = 0.3

    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance
    
    def deposit(self,num):
        self.balance += num
        print(f"New balance:{self.balance}")
    
    def withdraw(self,num):
        if(num<=self.balance):
            self.balance -= num
            print(f"New balance:{self.balance}")
        else:
            print("You have reached your overdraft limit")

    def add_interest(self):
        self.balance += self.balance*self.interest_rate
        print(f"New balance:{self.balance}")

    
class StudentAccount(BankAccount):

    def withdraw(self,num):
        #dont allow to overdraft (whats dat)
        if(num<=1000 and num <= self.balance):
            self.balance -= num
            print(f"New balance:{self.balance}")
        else:
            print("You have reached your overdraft limit")


adult = BankAccount("Bobert",90909,300)

adult.deposit(100)

adult.withdraw(200)

adult.add_interest()

student = StudentAccount("Ann",80808,1200)

student.deposit(200)

student.withdraw(1100)

student.add_interest()

student.withdraw(100)



