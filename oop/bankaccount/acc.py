class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath , 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        if(amount > balance):
            print("Insufficent Balance")
            return
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def fetch_balance(self):
        return self.balance

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))



class Checking(Account):  # Inheriting from class Account
    """ This class generates checking account objects """   # is a doc string of this class (intentation important)

    fee = 1  # class variable is for all instances created for this class
    type = "checking"

    def __init__(self, filepath):
        Account.__init__(self, filepath)   # Initializing the base class

    def tranfer(self, amount):
        self.balance = self.balance - amount - self.fee     # instance variable




checking = Checking("bankaccount\\balance.txt")
print(checking.balance)
checking.tranfer(100)
checking.commit()
print(checking.balance)
print(checking.__doc__)
