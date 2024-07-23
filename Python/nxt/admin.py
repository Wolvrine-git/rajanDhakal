import os
from datetime import datetime
import Customer_form as C
import generate_statement as G
def Admin():
    print("----Admin----")
    while True:
        menu = ''' 
    1. Create Staff Account
    2. Edit Staff Details
    3. Create Customer Account
    4. Edit Customer Details
    5. Generate Customer Statement
    6. List all Staff
    7. List all Customers
    8 .Return to main menu'''
        print(menu)
        choice  = input("Enter your choice(1-8): ")


        if choice == "1":
            last_acc = 111
            while True:
                try:
                    with open(F"Staff/{last_acc}.txt" , 'x') as f :
                        staff_name = input("Enter staff_name :")
                        staff_address = input("Enter staff_address :")
                        while True:
                            staff_Contact = input("Enter staff_Contact :")

                            if len(staff_Contact)!=10 or not staff_Contact.isdigit():
                                print("Please Enter 10 digit number")
                            else:
                                break # break from contact 


                        staff_Citizenship = input("Enter staff_Citizenship :")
                        staff_password = input("Enter staff_password :")
                        f.write(f"Staff_Id:{last_acc}\n")
                        f.write(f"staff_name: {staff_name}\n")
                        f.write(f"staff_address: {staff_address}\n")
                        f.write(f"staff_Contact: {staff_Contact}\n")
                        f.write(f"staff_Citizenship: {staff_Citizenship}\n")
                        f.write(f"staff_password: {staff_password}")
                        
                        print(f"Staff ID is {last_acc}")
                        input("Enter any key to go back....")
                            
                    break # break for to stop the continouse loop after creating a file
                except FileExistsError:
                    last_acc+=1

        elif choice == "2":
           while True:
            Staff_ID = input("Enter the staff Id to edit : ")
            if os.path.exists(f"Staff/{Staff_ID}.txt"):
                with open(f"Staff/{Staff_ID}.txt" , 'r') as f :
                    lines = f.readlines()
                    while True :
                        print("1.Edit Address")
                        print("2.Edit Contact")
                        print("3.Edit password")
                        print("4.Go Back")
                        choice = input("Enter your Choice :")
                        if choice == "1":
                            new_address = input("Enter the new address : ")
                            lines[2] = f"staff_address: {new_address}\n"
                            with open(f"Staff/{Staff_ID}.txt" , 'w') as f :
                                f.writelines(lines)
                            with open(f"Staff/{Staff_ID}.txt" , 'r') as f :
                                    a = f.read()
                                    print("------------------")
                                    print(a)
                                    print("------------------")
                                    print("Address updated...\n")

                        elif choice =="2":
                            new_contact = input("Enter the new Contact : ")
                            
                            lines[3] = f"staff_Contact: {new_contact}\n"
                            with open(f"Staff/{Staff_ID}.txt" , 'w') as f :
                                f.writelines(lines)
                            with open(f"Staff/{Staff_ID}.txt" , 'r') as f :
                                    a = f.read()
                                    print("------------------")
                                    print(a)
                                    print("------------------")
                                    print("Contact updated...\n")

                        elif choice =="3":
                           while True:
                             staffPassword = input("Enter the staff password :")
                             password = lines[-1].split(":")[1].strip()

                             if staffPassword == password:
                                new_password = input("Enter the new password : ")
                                lines[-1] = f"staff_password: {new_password}\n"
                                with open(f"Staff/{Staff_ID}.txt" , 'w') as f :
                                    f.writelines(lines)
                                with open(f"Staff/{Staff_ID}.txt" , 'r') as f :
                                    a = f.read()
                                    print("------------------")
                                    print(a)
                                    print("------------------")
                                    print("Password updated...\n")
                                break # if login is successful it will break the loop 
                             else:
                                 print("Password Didn't matched")

                        elif choice =="4":
                            break # return back to menu
                break # after the Id is found this break will stop the loop 
            else:
                print("No Staff Id found..")
            
        elif choice == "3":
            
            last_acc=888
            if not os.path.exists("Customers"):
                os.mkdir("Customers")
            C.Customer_form()
            
            with open("new_regestration_customer.txt" , 'r') as f :
                print("------------")
                a = f.read()
                print(a)
                print("------------")
                input("Enter any key to continue")
            while True :
                try:
                    if not os.path.exists(f"Customers/{last_acc}"):
                        os.mkdir(f"Customers/{last_acc}")
                    with open(f"Customers/{last_acc}/{last_acc}.txt" , 'x') as f :
                         f.writelines(f"Customer_ID : {last_acc}\n{a}")
                         print(f"Customer Account Number is {last_acc}")
                    break
                except FileExistsError:
                    last_acc+=1


        elif choice =="4":
           while True:
            Customer_ID = input("Enter the Customer Id to edit : ")
            if os.path.exists(f"Customers/{Customer_ID}/{Customer_ID}.txt"):
                with open(f"Customers/{Customer_ID}/{Customer_ID}.txt" , 'r') as f :
                    lines = f.readlines()
                    while True :
                        print("1.Edit Address")
                        print("2.Edit Contact")
                        print("3.Edit password")
                        print("4.Go Back")
                        choice = input("Enter your Choice :")
                        if choice == "1":
                            new_address = input("Enter the new address : ")
                            lines[2] = f"Customer_address: {new_address}\n"
                            with open(f"Customers/{Customer_ID}/{Customer_ID}.txt" , 'w') as f :
                                f.writelines(lines)
                            with open(f"Customers/{Customer_ID}/{Customer_ID}.txt" , 'r') as f :
                                    a = f.read()
                                    print("------------------")
                                    print(a)
                                    print("------------------")
                                    print("Address updated...\n")

                        elif choice =="2":
                            new_contact = input("Enter the new Contact : ")
                            lines[2] = f"Customer_Contact: {new_contact}\n"
                            with open(f"Customers/{Customer_ID}/{Customer_ID}.txt" , 'w') as f :
                                f.writelines(lines)
                            with open(f"Customers/{Customer_ID}/{Customer_ID}.txt" , 'r') as f :
                                    a = f.read()
                                    print("------------------")
                                    print(a)
                                    print("------------------")
                                    print("Contact updated...\n")

                        elif choice =="3":
                           while True:
                             CustomerPassword = input("Enter the Customer password :")
                             password = lines[-1].split(":")[1].strip()

                             if CustomerPassword == password:
                                new_password = input("Enter the new password : ")
                                lines[-1] = f"Customer_password: {new_password}\n"
                                with open(f"Customers/{Customer_ID}/{Customer_ID}.txt" , 'w') as f :
                                    f.writelines(lines)
                                with open(f"Customers/{Customer_ID}/{Customer_ID}.txt" , 'r') as f :
                                    a = f.read()
                                    print("------------------")
                                    print(a)
                                    print("------------------")
                                    print("Password updated...\n")
                                break # if login is successful it will break the loop 
                             else:
                                 print("Password Didn't matched")

                        elif choice =="4":
                            break # return back to menu
                break # after the Id is found this break will stop the loop 
            else:
                print("No Customer Id found..")
        elif choice == "5":
            print("---Generate Customer Statement---")
            while True:
                try:
                    Cust_ID = input("Enter Customer ID :")
                    
                    with open(f"Customers/{Cust_ID}/{Cust_ID}.txt" , 'r') as f :
                        lines = f.readlines()
                        password = lines[-1].split(":")[1].strip()
                        while True:
                            try:
                                Cust_pass = input("Enter Customer Password :")
                                if Cust_pass == password:
                                    str_date = datetime.strptime(input("Enter Start Date (YYYY-MM-DD): "),"%Y-%m-%d").date()
                                    end_date = datetime.strptime(input("Enter End Date (YYYY-MM-DD): "),"%Y-%m-%d").date()
                                    G.Statement(Cust_ID,str_date,end_date)
                                    
                                    input("Enter any key to contiue....")
                                    break
                                else:
                                    print("Wrong password Try Again!")
                            except ValueError:
                                print("Enter a valid date format..")
                    break
                
                except FileNotFoundError:
                    print("Customer Account Not Found")
        elif choice == "6":
            print("---Staff List---")
            list_all_staff = os.listdir("Staff")
            for name in list_all_staff:
                print(name)
            input("Enter any to continue ..")

        elif choice == "7":
            print("---Customers List---")
            list_all_customers = os.listdir("Customers")
            for name in list_all_customers:
                print(name)
            input("Enter any to continue ..")

        elif choice =="8":
            return
        else:
            print("Enter a valid choice...")

