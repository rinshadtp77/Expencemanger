from helper import *
from fileop import *
s=0
data=read_expences()
set_expences(data)
while(s==0):
    print("=====Menu=====")
    print("1=> For Insert")
    print("2=> For Show")
    print("3=> For Delete")
    print("4=> For Update")
    opt=int(input("Enter the option"))
    if(opt==1):
        create_expence()
    if(opt==2):
        show_expences()
    if(opt==3):
        delete_expence()
    if(opt==4):
        update_expence()  
    s=int(input("Do you want to continue? press 0 For Yes"))
    if(s!=0):
        d1=get_expences()
        write_expences(d1)
