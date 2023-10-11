def valbankname(bankName):
    bankList=['ICICI', 'HSBC', 'Axis', 'Punjab National Bank', 'Standard Chartered']
    if bankName in bankList:
        return 1
    else:
        return 0
        

def valAccNo(AccNo):
    if(AccNo.isnumeric()):
        return 1
    else:
        return 0
        
def valage(age):
    if(age>0):
        return 1
    else:
        return 0
        
def valname(accName): 
    if accName.istitle()==True:
        return 1
    else: 
        return 0

def valcity(city): 
    if city.istitle()==True and city.isalpha()==True:
        return 1
    else: 
        return 0
            
def valgender(gen):
    l=['M','F']
    if gen in l:
        return 1
    else:
        return 0
        
        
def valtype(typeAcc):
    l=['Savings','Current','Deposit']
    if typeAcc in l:
        return 1
    else: 
        return 0


def valbal(bal):
    if bal>0:
        return 1
    else:
        return 0

def valmob(mn):
    if len(mn)==10 and mn.isdigit()==True:
        return 1
    else:
        return 0        
        
def valpan(pan):
    y=pan[0:5]
    x=pan[9:10]
    t=pan[5:9]
    if len(pan)==10 and pan.isupper()==True and y.isalpha()==True and x.isalpha()==True and t.isdigit()==True:       
        return 1    
    else:          
        return 0
        
def valaadhar(an):
    if len(an)==12 and an.isdigit()==True:
        return 1
    else:
        return 0