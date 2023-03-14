# Assignment: Bank Account

# If you imagine a banking system, and how the data is modeled, you may think, well, everything should be tied to the customer, in other words, the user. But users have accounts, and accounts have balances. This gives us the idea that maybe an account is its own class apart from the user class. But as we stated, it is not completely independent of the User class; accounts only exist because users open them.

# For this assignment, don't worry about putting any user information in the BankAccount class. We'll take care of that in the next lesson!

# Let's first just get some more practice writing classes by writing a new BankAccount class.

# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
# This means we need a class that looks something like this:

class BankAccount:

    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

    @classmethod
    def all_accounts(cls):
        cls.all_accounts = cls.all_accounts
        print(cls.all_accounts)
        
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
        # your code here
    def withdraw(self, amount):
        self.balance -= amount 
        print(self.balance)
        return self
        # your code here
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
        return self
        # your code here
    def yield_interest(self):
        self.yield_interest = self.balance * self.int_rate
        print(self.yield_interest)
        return self
        
        # your code here

account1 = BankAccount(.03, 500)
account2 = BankAccount(.05, 200)

# account1.deposit(20)
# account1.deposit(100)
# account1.deposit(50)
# account1.withdraw(150)
# account1.yield_interest()
# account1.display_account_info()

account1.deposit(20).deposit(100).deposit(50).withdraw(150).yield_interest().display_account_info()

# account2.deposit(400)
# account2.deposit(35)
# account2.withdraw(100)
# account2.withdraw(25)
# account2.withdraw(30)
# account2.withdraw(100)
# account2.yield_interest()
# account2.display_account_info()

account2.deposit(400).deposit(35).withdraw(100).withdraw(25).withdraw(30).withdraw(100).yield_interest().display_account_info()
                                        
BankAccount.all_accounts()