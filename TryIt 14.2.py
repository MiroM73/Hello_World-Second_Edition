# coding=utf-8
# Make a class definition for a BankAccount.
# It should have attributes for its name (astring), account number (a string or integer),
# and balance (a float). It should have methods to display the balance,
# make deposits, and make withdrawals.

# Make a class called InterestAccount that earns interest. It should be a subclass of
# BankAccount (so it inherits the attributes and methods). It should also have an
# attribute for interest rate and a method to add interest. To keep things simple,
# assume that the addInterest() method will be called once each year to calculate
# the interest and update the balance.

# the next line was added because EUR symbol is used in the script
# coding=utf-8

class BankAccount:
    def __init__(self, name, accNumber, balance):
        self.name = str(name)
        self.accNumber = str(accNumber)
        self.balance = float(balance)

    def __str__(self):
        msg = "Bank Account name: " + self.name + "\n"
        msg += "Account number: " + str(self.accNumber) + "\n"
        msg += "Account balance: " + str(self.balance) + " €"
        return msg

    def displayBalance(self):
        print "Actual account balance: " + str(self.balance) + " €"

    def deposit(self, amount):
        print "Deposit account: ", amount
        self.balance += amount

    def withdraw(self, amount):
        print "Withdraw account: ", amount
        self.balance -= amount

class InterestBankAccount(BankAccount):
    def __init__(self, name, accNumber, balance, interestRate):
        BankAccount.__init__(self, name, accNumber, balance)
        self.interestRate = interestRate

    # def __str__(self):
    #     BankAccount.__str__(self)
    #     msg1 = "interestRate: " + str(self.interestRate * 100) + " %"
    #     return msg1

    def addInterest(self):
        print "Adding interest: ", self.interestRate * 100, "%"
        interest = self.balance * self.interestRate
        self.deposit(interest)

myBankAccount = BankAccount("Miroslav Misik", 3723421371, 10000)
myInterestAccount = InterestBankAccount("Miroslav Misik IR", "3723421371IR", 20000, 0.02)

print "myBankAccount"
print myBankAccount
myBankAccount.deposit(1000)
myBankAccount.displayBalance()
print
print "myInterestAccount"
print myInterestAccount
myInterestAccount.withdraw(1000)
myInterestAccount.displayBalance()
myInterestAccount.deposit(10000)
myInterestAccount.displayBalance()
myInterestAccount.addInterest()
myInterestAccount.displayBalance()
print
print "myBankAccount"
print myBankAccount
myBankAccount.deposit(1000)
myBankAccount.displayBalance()



