#---------------------------------------
#task 2: Job application
#---------------------------------------
print("Welcome to our Job application")
x = input("Do you know Python programming?(yes/no)").lower().strip()
y = float(input("How many years of experience or projects does he have? (Enter a number)"))
z = input("Do you have a computer science degree or have you completed an intensive bootcamp?(yes/no)").lower().strip()
if x == "yes" and (y >= 2 or z == "yes" ):
 print("Congratulations! You have been accepted to the next stage of interviews.")
else:
 print("Sorry, your current qualifications do not match the job requirements.")