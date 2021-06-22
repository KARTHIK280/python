class Customer:
    def __init__(self,name,cid,branch):
        self.name=name
        self.cid=cid
        self.branch=branch
    def Details(self):
        print("Customer Details:")
        print("Name:",self.name)
        print("Customer ID:",self.cid)
        print("Branch Name:",self.branch)

class AccountDetails(Customer):
    def __init__(self,name,cid,branch):
        self.balance=0
        super().__init__(name,cid,branch)
    def Deposite(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print("The Amount %d is deposited successfully. Remaining Balance Amount is:%d"%(self.amount,self.balance))
    def Withdraw(self,amount):
        self.amount=amount
        if(self.balance>self.amount):
            self.balance-=self.amount
            print("The balance amount is:",self.balance)
        else:
            print("Please check your balance!")
name=input("Enter Customer Name:")
cid=int(input("Enter Customer ID:"))
branch=input("Enter branch name:")
obj=AccountDetails(name,cid,branch)
while True:
    print("1.Deposite\n2.Withdrawl\n3.Customer Details")
    ch=int(input("Enter Choice:"))
    
    if(ch==1):
        amount=int(input("Enter Amount:"))
        print("Deposit:")
        obj.Deposite(amount)
    elif(ch==2):
        amount=int(input("Enter Amount:"))
        print("Withdrawl")
        obj.Withdraw(amount)
    elif(ch==3):
        obj.Details()
    else:
        print("End:")
        break


 
    
