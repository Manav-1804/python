class Bank:
    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello " ,cname, " Your Account Number " , acno, " IS Opened With " ,balance, " Rs. ")

    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("You Need Another ", amount-self.balance," Rs.  To Withdraw")
    def checkBalance(self):
        print("Current Balance : ",self.balance)

b1=Bank()
b1.openAccount("Manav",101,1000)

while True:
    print("-"*50)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    print("-"*50)
    choice=int(input("Enter Your Choice : "))
    print("-"*50)

    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("-"*50)
    elif choice==2:
        amount=int(input("Enter Withdraw Amount : "))
        b1.withdraw(amount)
        print("-"*50)
    elif choice==3:
        b1.checkBalance()
        print("-"*50)
    elif choice==4:
        print("Thank You Using Our Services...")
        print("-"*50)
        break
    else:
        print("Invalid Choice. Please Try Again")
        print("-"*50)
