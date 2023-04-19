class Bank_account:
    def __init__(self,intrate=0.03,balance=0):
        self.balance=balance
        self.intrate = intrate

    def deposit(self, amount):
        self.balance+=amount

    def withdraw(self, amount):
        if self.balance<amount:
            self.balance=-5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance-=amount

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        if self.balance>0:
            self.balance+=self.balance*self.intrate
        else:
            print("Account balance is negative")


class User:
    def __init__(self,name,email):
        self.name=name
        self.emial=email
        self.account=Bank_account()

    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
    
    def make_deposit(self,amount):
        self.account.deposit(amount)

    def display_user_balance(self):
        print( f"{self.name} account balance is: {self.account.balance}")

    def transfer_money(self,other_user,amount):
        self.account.balance-=amount
        other_user.account.balance+=amount


user1=User("Ibrahim","ibrahim@gmail.com")
user2=User("Taleen","taleen@gmail.com")
user3=User("Elon","Elon@twitter.com")


user1.make_deposit(500)
user1.display_user_balance()
