class Bank_account:
    def __init__(self,intrate,balance=0):
        self.balance=balance
        self.intrate = intrate

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if self.balance<amount:
            self.balance=-5
            print("Insufficient funds: Charging a $5 fee")
            return self
        else:
            self.balance-=amount
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance>0:
            self.balance+=self.balance*self.intrate
            return self
        else:
            print("Account balance is negative")
            return self

account1=Bank_account(0.05,1000)
account2=Bank_account(0.03,2000)
account1.deposit(200).deposit(300).deposit(250).withdraw(500).yield_interest().display_account_info()
account2.deposit(1000).deposit(500).withdraw(250).withdraw(300).withdraw(200).withdraw(400).yield_interest().display_account_info()