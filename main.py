from validate import * 
import random
from datetime import datetime

class Bank:
    BankDict={}
    def __init__(self, bankname, IFSC, account_type, customer_name, mob, DOB, age, gender, address, city, pan, aadhar, account_number, balance):
        self.bankname = bankname
        self.IFSC = IFSC
        self.account_type = account_type
        self.customer_name = customer_name
        self.mob=mob
        self.DOB = DOB
        self.age = age
        self.gender = gender
        self.address = address
        self.city = city
        self.pan = pan
        self.aadhar = aadhar
        self.account_number = account_number
        self.balance = balance
        
        if self.bankname in self.BankDict.keys():
            self.BankDict[self.bankname].append(self.customer_name)
        else:
            self.BankDict[self.bankname] = [self.customer_name]

    def display(self):
        print(self.bankname,self.IFSC, self.customer_name,self.account_number, self.account_type, self.mob, self.age, self.address, self.balance)
    
    def updateaddress(self,account_number):
        newad=input("Enter new Address: ")
        self.address=newad
        print(self.address)

    def updatename(self,account_number):
        newname=input("Enter new Name: ")
        self.customer_name=newname
        print(self.customer_name)

    def deposit(self, account_number):
        amount=int(input("Enter the amount to deposit: "))
        self.balance += amount
        print(amount," has been deposited in your account.")
        print("Current Balance is: ",self.balance)

    def withdraw(self, account_number):
        amount=int(input("Enter the amount to Withdraw: "))
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(amount," has been withdrawn from your account.")
            print("Current Balance is: ",self.balance)

    def showbal(self, account_number):
        print("Current Balance is: ",self.balance)
    
    @classmethod
    def BankWiseDet(self):
        for k,v in self.BankDict.items():
            print(k,"=",v)
        

CustList=[]

ifscDict={'ICICI':'ICIC0002331','HSBC':'HSBC0002331','Axis':'AXIS0002331','Punjab National Bank':'PUNB0002331','Standard Chartered':'SCBL0002331'}

def generateAccNo():
    account_number = random.randint(10**10, 10**11 - 1)
    return account_number
    
def calculate_age(DOB):
    today = datetime.today()
    age = today.year - DOB.year - ((today.month, today.day) < (DOB.month, DOB.day))
    return age
    
while True:
    print("\nBank Management System:")
    print("1. Create Account")
    print("2. Display Details")
    print("3. Delete Account")
    print("4. Update Account Details")
    print("5. Deposit")
    print("6. Withdraw")
    print("7. Funds Transfer")
    print("8. Search Details of Account Holder")
    print("9. Balance Enquiry")
    print("10. Bank Wise Details")
    print("11. Exit")
    
    ch=int(input("Enter your choice: "))
    if ch==1:
        while True:                         
            bankname=input("Enter Bank Name [ICICI/HSBC/Axis/Punjab National Bank/Standard Chartered]: ") 
            if valbankname(bankname):
                break
            else:
                print("Invalid Name, Enter again")
        IFSC=ifscDict[bankname]
        print("IFSC code for this bank: ",IFSC)
        while True:
            account_type=input("Enter Account Type [Savings/Current/Deposit]: ")
            if valtype(account_type):
                break
            else:
                print("Invalid Type, Enter again")
        
        while True:
            customer_name=input("Enter Customer Name: ")
            if valname(customer_name):
                break
            else:
                print("Invalid Name, Enter again")
        while True:    
            mob=input("Enter Mobile No.: ")
            if valmob(mob):
                break
            else:
                print("Invalid Mobile No., Enter again")
        while True:
            date_input = input("Enter your birth date in the format DD-MM-YYYY: ")
            DOB = datetime.strptime(date_input, "%d-%m-%Y")
            age = calculate_age(DOB)
            print("Your age is: ",age)
            break
        while True:    
            gender=input("Enter Gender [M/F]: ")
            if valgender(gender):
                break
            else:
                print("Invalid Gender, Enter again")
        address=input("Enter Address: ")
        while True:
            city=input("Enter City: ")
            if valcity(city):
                break
            else:
                print("Invalid City, Enter again")
        while True:    
            pan=input("Enter PAN: ")
            if valpan(pan):
                break
            else:
                print("Invalid PAN, Enter again")
        while True:    
            aadhar=input("Enter Aadhar No.: ")
            if valaadhar(aadhar):
                break
            else:
                print("Invalid Aadhar No., Enter again")
        while True:
            account_number=generateAccNo()
            print("Your Account Number is: ",account_number)
            break
        balance=0
        print("Your Balance is: ",balance)    
        obj=Bank(bankname, IFSC, account_type, customer_name, mob, DOB, age, gender, address, city, pan, aadhar, account_number, balance)  #invoke constructor
        CustList.append(obj)
    
    elif ch==2:
        for i in CustList:   #display each object details from list (array) of objects
            i.display()
    
    elif ch==3:
        print("Press A to delete record by Account Number: ")
        print("Press B to delete record by Name: ")
        choice=input("Enter your choice: ")
        if choice=='A':
            p=int(input("Enter Account Number to be deleted: "))
            for i in CustList:
                if i.account_number==p:
                    CustList.remove(i)
        elif choice=='B':
            p=input("Enter Name to be deleted: ")
            for i in CustList:
                if i.customer_name==p:
                    CustList.remove(i)
    
    elif ch==4:
        print("Press A to Update Name: ")
        print("Press B to Update Address: ")
        choice=input("Enter your choice: ")
        if choice=='A':
            p=int(input("Enter Acc No. whose Name needs to be updated:"))
            for i in CustList:
                if i.account_number==p:
                    i.updatename(account_number)
        if choice=='B':
            p=int(input("Enter Acc No. whose Address needs to be updated: "))
            for i in CustList:
                if i.account_number==p:
                    i.updateaddress(account_number)
    
    elif ch==5:
        p=int(input("Enter Acc No. to Deposit:"))
        for i in CustList:
            if i.account_number==p:
                i.deposit(account_number)

    elif ch==6:
        p=int(input("Enter Acc No. to Withdraw:"))
        for i in CustList:
            if i.account_number==p:
                i.withdraw(account_number)

    elif ch==7:
        reciever=int(input("Enter Reciever's account number: "));
        flag = False
        flag1 = False
        for i in CustList:
            if i.account_number == reciever:
                flag1=True
                sender=int(input("Enter Sender's account number: "));
                for j in CustList:
                    if j.account_number==sender:
                        amount = int(input("Enter the Amount to be transfer ?? "))
                        if j.balance < amount:
                            print("Insufficent balance ")
                        else:
                            i.balance = i.balance + amount
                            j.balance = j.balance - amount 
                        flag = True 
                        break 
                if flag == True:
                    break 
        if flag1==False:
            print("Reciever Account number is invalid ")
                           
    elif ch==8:
        print("Press A to search by Account Number: ")
        print("Press B to search by Name: ")
        print("Press C to search by Account Type: ")
        choice=input("Enter your choice: ")
        if choice=='A':
            p=int(input("Enter Account Number to be searched: "))
            for i in CustList:
                if i.account_number==p:
                    i.display()
        elif choice=='B':
            p=input("Enter Name to be searched: ")
            for i in CustList:
                if i.customer_name==p:
                    i.display()
        elif choice=='C':
            p=input("Enter Account Type to be searched: ")
            for i in CustList:
                if i.account_type==p:
                    i.display()
        else:
            print("Invalid Choice")
    
    elif ch==9:
        p=int(input("Enter Acc No. to Show Balance:"))
        for i in CustList:
            if i.account_number==p:
                i.showbal(account_number)

    elif ch==10:
        Bank.BankWiseDet()

    elif ch==11:
        break
    else:
        print("Invalid Choice")