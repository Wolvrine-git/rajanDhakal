def current():
    print("----Current Type---")
    def_password = "000"
    customer_name = input ( "Enter Your name :" )
    customer_address = input ( "Enter Your Address :" )
    while True:
        customer_number = input ( "Enter Your number :" )
        if len(customer_number)!=10 or  not customer_number.isdigit():
            print("Enter a valid number")
        else:
            break
    customer_citzno = input ( "Enter Your Citizenship No :" )
    while True:
        min_amt = int(input("Enter min Rs.500 :"))
        if min_amt < 500 or not customer_number.isdigit():
            print("Amt is low Please add Rs.500")
        else:
            break
    with open("new_regestration_customer.txt" , 'w') as f :
        f.write ( f"customer_name: {customer_name}\n" )
        f.write ( f"customer_address: {customer_address}\n" )
        f.write ( f"customer_Number: {customer_number}\n" )
        f.write ( f"customer_citizenship_number: {customer_citzno}\n" )
        f.write ( f"Account Type: Current\n" )
        f.write ( f"Total-amt: ${min_amt}\n" )
        f.write (  f"Customer_password: {def_password}")


def Saving():
    print("----Saving Type---")
    def_password = "000"
    customer_name = input ( "Enter Your name :" )
    customer_address = input ( "Enter Your Address :" )
    while True:
        customer_number = input ( "Enter Your number :" )
        if len(customer_number)!=10 or  not customer_number.isdigit():
            print("Enter a valid number")
        else:
            break
    customer_citzno = input ( "Enter Your Citizenship No :" )
    while True:
        min_amt = int(input("Enter min Rs.100 :"))
        if min_amt < 100 or not customer_number.isdigit():
            print("Amt is low Please add Rs.100")
        else:
            break
    with open("new_regestration_customer.txt" , 'w') as f :
        f.write ( f"customer_name: {customer_name}\n" )
        f.write ( f"customer_address: {customer_address}\n" )
        f.write ( f"customer_Number: {customer_number}\n" )
        f.write ( f"customer_citizenship_number: {customer_citzno}\n" )
        f.write ( f"Account Type: Savings\n" )
        f.write ( f"Total-amt: ${min_amt}\n" )
        f.write (  f"Customer_password: {def_password}")

def Customer_form():
    print("--------Customer Login Form----------\n")
    print("1.For Current Account Type")
    print("2.For Saving Account Type")
    choice = input("Enter your Choice :")
    if choice == "1":
        current()
    elif choice =="2":
        Saving()
    else:
        print("Enter a valid Choice")
    

