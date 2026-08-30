print("====================================")
print("Welcome to the atm system")
print("====================================")
pin = 1357
user_pin = int(input("enter your pin: \n"))
if user_pin == pin:
    print("Login Sucessful")
else:
    print("Wrong pin")
print("\n ========== ATM MENU ===========") 
print("1.Check balance")
print("2.Deposite")
print("3.Withdraw")
print("4.Exit")
choice = input("Enter your choice: \n")
if choice == "1":
    print("Your balance is 10000")