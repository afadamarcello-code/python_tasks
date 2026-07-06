#---------------------------------------
# task 3: ATM
#---------------------------------------
print("Hello, I am a very smart ATM Simulator! ")
password = 1234
balance = 5000
code = int(input("Entey your card PIN:"))
if code == password:
    process =int(input("For cash withdraw write 1\n To check you balance write 2:\n"))
    if process == 2:
        print(f"your card balance is {balance}$")
    elif process == 1:
        withdraw = int(input("Enter the amount you want to withdraw:"))
        if withdraw > balance:
            print("Sorry, your balance is insufficient.")
        else:
            print(f"The transaction was successful. Your remaining balance is:{balance-withdraw}$")
    else:
        print("Invalid choice. Operation canceled.")
else:
    print("Wrong PIN, transaction rejected.")
