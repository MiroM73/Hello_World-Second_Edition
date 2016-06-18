# coding=utf-8
"""  Make a class definition for a BankAccount.
It should have attributes for its name (a string), account number (a string or integer),
and balance (a float). It should have methods to display the balance,
make deposits, and make withdrawals. """

class BankAccount:
    def __init__(self, name, accNumber, balance):
        self.name = name
        self.accNumber = accNumber
        self.balance = balance

    def __str__(self):
        msg = "Bank Account name: " + self.name + "\n"
        msg += "Account number: " + str(self.accNumber) + "\n"
        msg += "Account balance: " + str(self.balance) + " €"
        return msg

    def display(self):
        msg = "Actual account balance: " + str(self.balance) + " €"
        return msg

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

myBankAccount = BankAccount("Miroslav Misik", 3723421371, 11250.23)

print myBankAccount
print "Deposit 2000 €"
myBankAccount.deposit(2000)
print myBankAccount.display()
print "Withdraw 500"
myBankAccount.withdraw(500)
print myBankAccount.display()




