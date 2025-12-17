Balance=8000

def check_Balance():
    return f"Your Current Balance is {Balance}"

def deposite():
    global Balance
    amount=int(input("Enter Your Amount :"))
    if amount>0:
        Balance+=amount
        return f"Deposite Successful...Your total Balance is {Balance}"
    
def withdrawl():
    global Balance
    amount=int(input("Enter Your Amount :"))
    if amount<=0:
        return "Invalid Amount"
    elif amount>Balance:
        return "Insufficient Balance !"
    else:
        Balance-=amount
        return f"{amount} has been withdrawl succsefully...You'r Total Balance is {Balance}"
    
def options():
    print("=====WELCOME TO ATM=====")
    print()
    print("1.Check Balance")
    print("2.Deposite")
    print("3.Withdrawl")
    print("4.Exit")

    print()



    user=int(input("Select your Options : "))

    print()
    
    if user==1:
        return check_Balance()
    
    elif user==2:
        return deposite()
    
    elif user==3:
        return withdrawl()
    
    elif user==4:
        return "Thank You for Using ATM"
    
    else:
        return "Invalid selecion"
    
print(options())