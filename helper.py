expences=[]
def create_expence():
    payee=input("Enter Payee")
    amount=input("Enter Amount")
    purpose=input("Enter Purpose")
    dt=input("Enter Date")
    expences.append((payee,amount,purpose,dt))
def show_expences():
    #print(payee+" "+amount+" "+purpose+" "+dt)
    #print(expences)
    for item in expences:
        print(item)
def delete_expence():
    id=int(input("Enter the index you want to delete"))
    del expences[id]
def update_expence():
    id=int(input("Enter the index you want to update"))
    payee=input("Enter Payee")
    amount=input("Enter Amount")
    purpose=input("Enter Purpose")
    dt=input("Enter Date")
    expences[id]=(payee,amount,purpose,dt)
