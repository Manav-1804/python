class BankAccount:
    def __init__(self,account_holder,balance):

        self.account_holder = account_holder

        self.__balance = balance


    def get_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if 0< amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid Withdrawal amount:")

account = BankAccount("Jhon Doe",1000)

print(account.account_holder)

#print(account.balance)

print(account.get_balance())

account.deposit(500)
print(account.get_balance())

account.withdraw(200)
print(account.get_balance())

print(account._BankAccount__balance)
