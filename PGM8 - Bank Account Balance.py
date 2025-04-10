class Account:

    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount ,"debited....")

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount ,"credited...")

    def show_balance(self):
        print("Your balance is....",self.balance)
    
Acc1=Account(6000,12345)
Acc1.debit(3000)
Acc1.credit(500)
Acc1.show_balance()

