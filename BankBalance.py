class Bank:
    def OpenAccount(self):
        self.__acno=input("Enter Account Number:")
        self.__name=input("Enter Name:")
        self.__balance=int(input("Enter Balance:"))
    def ShowAccount(self):
        print(self.__acno,self.__name,self.__balance)
    def searchById(self,id):
        if(self.__acno==id):
            return True
        else:
            return False
    def Depsit(self):
        amt=int(input("Enter ammount u want to deposit:"))
        self.__balance=self.__balance+amt
    def Withdrawal(self):
        amt=int(input("Enter amt u want to withdrawal:"))
        if (self.__balance>amt):
            self.__balance=self.__balance-amt
        else:
          print("Less balance")
cl=[]
n=int(input("Enter no. of employee:"))
for i in range(n):
    C=Bank()
    C.OpenAccount()
    cl.append(C)
while True:
    print("main menu:\n1]Display all customers:\n2]Search by Account number\n3]Deposit\n4]Withdrawal\n5]Exit")
    ch=int(input("Enter your choice:"))
    if (ch==1):
        for c in cl:
            c.ShowAccount()
    elif (ch==2):
        found=False
        id=input("Enter id u want to search :")
        for c in cl:
            found=c.searchById(id)
            if (found):
                c.ShowAccount()
                break
            if(not found):
                print("Record not found")
    elif (ch==3):
        found=False
        id = input("Enter id u want to search deposit money")
        for c in cl:
            found=c.searchById(id)
            if (found):
                c.ShowAccount()
                c.Depsit()
                break
        if (not found):
                print("Record not found")
    elif (ch == 4):
        found = False
        id = input("Enter ID u Want to Search to Withdraw Money:")
        for c in cl:
            found=c.searchById(id)
            if (found):
                c.ShowAccount()
                c.Withdrawal()
                break
        if (not found):
            print("Record Not Found")
    elif (ch==5):
        print("Good Bye")
        break
    elif (ch>=6):
        print("Invalid choice")






