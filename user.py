# Assignment: User
# For this assignment you will create the user class and add a couple methods!

# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

# first_name
# last_name
# email
# age
# Also include default attributes:

# is_rewards_member - default value of False
# gold_card_points = 0
# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
# Ninja Bonuses:

# Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." and return False, otherwise return True.
# Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.


class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(self.is_rewards_member, self.gold_card_points)
        else:
            print(f"{self.first_name} {self.last_name} is already a Rewards Member.")

    def spend_points(self, amount):
        if self.gold_card_points > 0:
            self.gold_card_points = self.gold_card_points - amount
            print(self.gold_card_points)
        else:
            print("You do not have enough points in your account.")

    

new_user = User("John", "Doe", "ieorflj@gmail.com")
new_user.display_info()
new_user.enroll()
new_user.spend_points(50)

new_user2 = User("Jane", "Doe", "lijdfieww@gmail.com")
new_user3 = User("Harry", "Styles", "dlfjldj@gmail.com")

new_user2.enroll()
new_user2.spend_points(80)


new_user.display_info()
new_user2.display_info()
new_user3.display_info()

new_user.enroll()
new_user3.spend_points(40)






