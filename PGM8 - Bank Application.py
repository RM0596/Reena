
class Account:

    def __init__(self,bal,acc,acc_pass):
        self.balance=bal
        self.account_no=acc
        self.__acc_pass=acc_pass

    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount ,"debited....")

    def credit(self,amount):
        self.balance += amount
        print("Rs.", amount ,"credited...")

    def show_balance(self):
        print("Your balance is....",self.balance)

    def reset_pass(self):
        print(self.__acc_pass)
    
Acc1=Account(6000,12345,72928)
print(Acc1.balance,Acc1.account_no)

#Private Attribute
#print(Acc1.__acc_pass)

print(Acc1.reset_pass())
Acc1.debit(3000)
Acc1.credit(500)
Acc1.show_balance()

