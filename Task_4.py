# ========== PHASE 1: SKELETON ==========

accounts = {}

def Register():
    user= input("choose a username:\n").strip().lower()
    if not user:
        print("username can't be empty")  
        return  
    elif user in accounts:
        print("user already exist")
        return  

    pw= input("choose your password:(6 characters)\n")
    
    if len(pw) < 6:
        print("password must be at least 6 characters")
        return
    print("Account created successfully✅")
    accounts[user] ={"password": pw, "balance": 0}
 

def check_balance(user):
    print(f"Your account balance is {accounts[user]["balance"]} EGP")

def deposite(user):
    try:
        balance= float(input("How much to deposite: \n"))
    except ValueError:
        print("Kindly enter a number not text.")
        return
    
    if balance <= 0:
        print("Amount must be greater than zero.")
        return
    else:
        accounts[user]["balance"]+= balance
        print(f"Deposit successful! New balance:{accounts[user]["balance"]} EGP")

def Withdraw(user):
    try:
        amount = float(input("Enter the amount:"))
    except ValueError:
        print("Kindly enter a number not text.")  
        return
    
    if amount <= 0:
        print("Amount must be greater than zero.")
        return
    elif amount > accounts[user]["balance"]:
        print("Insufficient balance.")
        return
    else:
        accounts[user]["balance"]-= amount
        print(f"Successful cash withdrawal, your current balance {accounts[user]['balance']}")

def Transfer(user):
    try:
        recipient= str(input("Please enter the recipient's Username:\n")).strip().lower()
        if recipient not in accounts:
            print("Recipient does not exist.")
            return
    except ValueError:
        print("Enter a valid Username")
        return

    try:
        amount = float(input("Please enter the amount:\n"))
    except ValueError:
        print("Enter a valid amount")
        return
    
    if amount > accounts[user]["balance"]:
        print("Insufficient balance.")
        return
    elif recipient == user:
        print("You cannot transfer to yourself.")
        return
    else:
        accounts[user]["balance"] -= amount
        accounts[recipient]["balance"] += amount
        print(f"Successful  transction to {recipient}, your current balance {accounts[user]["balance"]}")

def Change_Password(user):
    old = input("Enter your old password\n")
    if old != accounts[user]["password"]:
        print("Wrong password")
        return
    else:
        new = input("choose your new password:(6 characters)\n")
        if len(new) < 6:
            print("password must be at least 6 characters")
            return
        else:
            accounts[user]["password"] = new
            print("New password updated")

    

def bank_menu(user):
    while True:
        order= input("="*20+"Bank Menu"+"="*20+"\n[1] Check Balance\n[2] Deposit\n[3] Withdraw\n[4] Transfer\n[5] Change Password\n[6] Logout\n")
        if order == "1":
            check_balance(user) 
        elif  order == "2":
            deposite(user)            
        elif  order == "3":
            Withdraw(user)
            
        elif  order == "4":
            Transfer(user)
            
        elif  order == "5":
            Change_Password(user)
        elif  order == "6":
                break
        else:
            print("Invalid choice. Please enter 1-6.")

                
def Login():
    user = input("username:\n").strip().lower()
    pw = input("password:\n")
    if user in accounts and accounts[user]["password"]== pw:
        print("login successful")
        bank_menu(user)
    else:
        print("wrong password or username")


def main ():
    print("="*20+"Welcome to Python bank"+"="*20)

    while True:
        choice= input("choose a number from the menu:\n[1] Register\n[2] Login\n[3] Exit\n")
        if choice =="1":
            Register()
        elif choice =="2":
            Login()
        elif choice == "3":
                print("Goodbye!")
                break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
