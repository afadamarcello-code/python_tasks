#---------------------------------------
#task 1: instant discount calculator
#---------------------------------------
print("-"*60)
print("#Welcome to our Discount calculator#")
print("-"*60)
X= float(input("enter your purchase amount:"))
if X < 100:
    disc = 0
if X < 500: 
    disc = 0.10
else:
    disc = 0.20

disc_value = disc * X
total = X - disc_value
print("-"*60)
print(f"your discount value is: {disc_value}$\n The total price after discount is: {total}")
