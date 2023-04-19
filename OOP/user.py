class User:
    def __init__(self, name, email):
        self.name = name
        self.emial = email
        self.account_balance = 0

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"{self.name} account balance is: {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


user1 = User("Ibrahim", "ibrahim@gmail.com")
user2 = User("Taleen", "taleen@gmail.com")
user3 = User("Elon", "Elon@twitter.com")

user1.deposit(500).deposit(1000).deposit(100).make_withdrawal(900).display_user_balance()

user2.deposit(500).deposit(1000).make_withdrawal(100).make_withdrawal(900).display_user_balance()

user3.deposit(2500).make_withdrawal(1000).make_withdrawal(100).make_withdrawal(900).display_user_balance()

user1.transfer_money(user3, 200)
user1.display_user_balance()
user3.display_user_balance()
