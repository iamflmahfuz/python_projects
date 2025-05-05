class Banking:
    def __init__(self, user_Name, initial_balance):
        self.name = user_Name
        self.balance = initial_balance
    def deposit(self,amount):
        if amount>0:
            self.balance = self.balance+amount
        return amount
    def get_balance(self):
        return self.balance

    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
            return amount
        else:
            return f"Insuffcient Balance."
ostad = Banking("Ostad",10000)
print(f"Account Name: {ostad.name}")
print(f"Initail Balance is: {ostad.balance}")
print(f"Deposit Balance is: {ostad.deposit(10000)}")
print(f"After Deposit,YOur Balance is: {ostad.get_balance()}")
print(f"Withdraw Balance is: {ostad.withdraw(2000)}")
print(f"After Withdraw,YOur Balance is: {ostad.get_balance()}")
