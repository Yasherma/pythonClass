class Bank:
    def __init__(self,Deltails):
        self.Deltails=Deltails
class Add:
    def __init__(self):
        self.Account=[]
    def Add_Account(self,Account):
        self.Account.append(Account)
    def Delete_Account(self,Account):
        self.Account.remove(Account)
    def Deposit(self,Account):
        self.Account.pop(Account)
class New_Account(Bank):
    def __init__(self,ADD,Delete,Deposit):
        self.Add=ADD
        self.Delete=Delete
        self.deposit=Deposit
    def display(self):
        return f"the all detele {self.Add}  {self.Delete}   {self.deposit}"
Std=Bank("RAMJI")
Std1=Bank("Sitaji")

emp1=Add()
emp1.Add_Account(Std)
emp1.Delete_Account(Std)
emp12=New_Account("shiv" ,"Account","Money")
emp12.display()

