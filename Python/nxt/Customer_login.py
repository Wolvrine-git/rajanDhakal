from datetime import datetime
import generate_statement as GST
def withdraw(ID):
    today = datetime.today().date()
    while True:
        try:
            amt = float(input("Enter the amount you want to withdraw: "))
            if amt < 0 :
                print("Enter a valid number")
            else:
                with open(f"Customers/{ID}/{ID}.txt", 'r') as f:
                    lines = f.readlines()
                    before_amt = float(lines[-2].split("$")[1].strip())  # Extract previous balance

                    if amt >= before_amt:
                        print("Cannot withdraw more than available balance.")
                    else:
                        total_amt = before_amt - amt
                        lines[-2] = f"Total-amt: ${total_amt:.2f}\n"

                        with open(f"Customers/{ID}/{ID}.txt", 'w') as f:
                            f.writelines(lines)

                        with open(f"Customers/{ID}/trans.txt", 'a') as f:
                            f.write(f"{today} :Withdraw = ${amt}\n")
                        
                        print(f"Successfully withdrew ${amt}. New balance: ${total_amt}")
            break
        
        except ValueError:
            print("Enter a valid amount.")

def deposit(ID):
    today = datetime.today().date()
    while True:
        try:
            amt = float(input("Enter the amount you want to deposit: "))

            with open(f"Customers/{ID}/{ID}.txt", 'r') as f:
                lines = f.readlines()
                before_amt = float(lines[-2].split("$")[1].strip())  # Extract previous balance
                total_amt = before_amt + amt
                lines[-2] = f"Total-amt: ${total_amt:.2f}\n"

            with open(f"Customers/{ID}/{ID}.txt", 'w') as f:
                f.writelines(lines)

            with open(f"Customers/{ID}/trans.txt", 'a') as f:
                f.write(f"{today} :Deposited = ${amt}\n")
            
            print(f"Successfully deposited ${amt}. New balance: ${total_amt}")
            break
        
        except ValueError:
            print("Enter a valid amount.")

def check_balance(ID):
    try:
        with open(f"Customers/{ID}/{ID}.txt", 'r') as f:
            lines = f.readlines()
            amt = lines[-2].split("$")[1].strip()
            total_amt = float(amt)
            print(f"Total balance is: ${total_amt:.2f}")
    
    except FileNotFoundError:
        print("No account found.")

def change_password(ID, cus_pass):
    chances = 3
    while chances > 0:
        passwd = input("Enter your Old password: ")
        with open(f"Customers/{ID}/{ID}.txt", 'r') as f:
            lines = f.readlines()
            if cus_pass == passwd:
                new_password = input("Enter your new Password: ")
                lines[-1] = f"Customer_password: {new_password}\n"

                with open(f"Customers/{ID}/{ID}.txt", 'w') as f:
                    f.writelines(lines)
                
                print("Password changed successfully.")
                return
            
            else:
                chances -= 1
                print(f"Password didn't match. {chances} chances left.")
    
    print("Contact bank for further assistance.")

def customer_login():
    print("-----Customer Login Section-----")
    while True:
        try:
            customer_ID = input("Enter your Account Number: ")

            with open(f"Customers/{customer_ID}/{customer_ID}.txt", 'r') as f:
                lines = f.readlines()
                password = lines[-1].split(":")[1].strip()
                name = lines[1].split(":")[1].strip()

                while True:
                    customer_pass = input("Enter your Password: ")
                    if customer_pass == password:
                        print(f"------Welcome {name.upper()}------")
                        while True:
                            print("\n1. Withdraw")
                            print("2. Deposit")
                            print("3. Check balance")
                            print("4. Change password")
                            print("5. Generate Statement")
                            print("6. Go back to main menu")
                            choice = input("Enter your Choice (1-5): ")

                            if choice == "1":
                                print("---Withdraw Section---")
                                withdraw(customer_ID)
                                input("Enter any key to go back....")
                            
                            elif choice == "2":
                                print("---Deposit Section---")
                                deposit(customer_ID)
                                input("Enter any key to go back....")
                            
                            elif choice == "3":
                                print("---Check Balance Section---")
                                check_balance(customer_ID)
                                input("Enter any key to go back....")
                            
                            elif choice == "4":
                                print("---Change Password Section---")
                                change_password(customer_ID, password)
                                input("Enter any key to go back....")

                            elif choice == "5":
                                print("---Generate Statement Section---")

                                
                                start_date = input("Enter start date (YYYY-MM-DD): ")
                                end_date = input("Enter end date (YYYY-MM-DD): ")
                                S= datetime.strptime(start_date,"%Y-%m-%d").date()
                                E= datetime.strptime(end_date,"%Y-%m-%d").date()
                                GST.Statement(customer_ID, S, E)
                                input("Enter any key to go back....")
                            
                            elif choice == "6":
                                break
                            
                            else:
                                print("Enter a valid choice (1-5)")
                        
                        break
                    
                    else:
                        print(" Wrong ID or Password ")
                
                break
        
        except FileNotFoundError:
            print("No Account Found")

