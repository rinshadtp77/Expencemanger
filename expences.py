s=0
expences=[]
while(s==0):
    print("=====Menu=====")
    print("1=> For Insert")
    print("2=> For Show")
    print("3=> For Delete")
    print("4=> For Update")
    opt=int(input("Enter the option"))
    if(opt==1):
        payee=input("Enter Payee")
        amount=input("Enter Amount")
        purpose=input("Enter Purpose")
        dt=input("Enter Date")
        expences.append((payee,amount,purpose,dt))
    if(opt==2):
        #print(payee+" "+amount+" "+purpose+" "+dt)
        #print(expences)
        for item in expences:
            print(item)
    if(opt==3):
        id=int(input("Enter the index you want to delete"))
        del expences[id]
    if(opt==4):
        id=int(input("Enter the index you want to update"))
        payee=input("Enter Payee")
        amount=input("Enter Amount")
        purpose=input("Enter Purpose")
        dt=input("Enter Date")
        expences[id]=(payee,amount,purpose,dt)

    s=int(input("Do you want to continue? press 0 For Yes"))
