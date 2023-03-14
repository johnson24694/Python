# Assignment: Users with Bank Accounts:

# Create a User class that has an association with the BankAccount class. You should not have to change anything in the BankAccount class.

# For example, from the User class we should be able to deposit money into the user's account:

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(int_rate=0.02, balance=0)
    
#     # other methods
    
#     def make_deposit(self, amount):
#     	# your code here
# copy
# But our User class does not have a self.account_balance attribute. What it does have is an instance of a BankAccount by the name of self.account. That means that we'll be mirroring the methods created in the BankAccount class like make_deposit (and other methods referencing self.account_balance). But we'll be calling on the BankAccount class to do most of the work! That's the goal of this assignment, and you may find that you do not have to add much logic if any.

# Remember in our User methods, we can now access the BankAccount class through our self.account attribute, like so:

# class User:
#     def example_method(self):
#         self.account.deposit(100)		# we can call the BankAccount instance's methods
#     	print(self.account.balance)		# or access its attributes


class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

        
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
        
    def withdraw(self, amount):
        self.balance -= amount 
        print(self.balance)
        return self
        
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
        return self
    
    def account_balance(self):
        print(self.balance)
        return self
        
    def yield_interest(self):
        self.yield_interest = self.balance * self.int_rate
        print(self.yield_interest)
        return self
    


class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdraw(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        self.account.account_balance()
        print(self.display_user_balance)


new_user = User("John Doe", "ieorflj@gmail.com")
new_user.make_deposit(50)
new_user.make_withdraw(25)
new_user.display_user_balance()
