class Bankaccount:
    def __init__(self,account_number):
        self.account_number=account_number
        self.balance=0
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            raise ValueError("Insufficient funds")
    def deposit(self,amount):
        self.balance+=amount
    def get_balance(self):
        return self.balance
def transfer_amount(u1,u2,amount):
    try:
        u1.withdraw(amount)
        u2.deposit(amount)
        return True
    except:
        return False

u1=Bankaccount("1234567892")
u2=Bankaccount("9876543211")
u1.deposit(200)
u2.deposit(50)
print("u1 :{}".format(u1.get_balance()))
print("u2 :{}".format(u2.get_balance()))
print(transfer_amount(u1,u2,20))
print("transfering money from u1 to u2")
print("u1 :{}".format(u1.get_balance()))
print("u2 :{}".format(u2.get_balance()))