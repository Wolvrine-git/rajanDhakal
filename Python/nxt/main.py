
import os 
import admin as A
import Customer_login as C
def main():
    if  not os.path.exists("super.txt"): # create superuser if not available
        with open("super.txt" , 'w') as f :
            f.write("admin-Id:1\nadmin-password:1")
    with open("super.txt" , 'r') as f: # read the value from the super.txt file
        lines = f.readlines()

    super_user_ID = lines[0].split(":")[1].strip() # get the 1st line of the of the file
    super_user_password = lines[1].split(":")[1].strip()# get the 2nd  line of file

    while True:
        print("1.Admin")
        print("2.Customer")
        print("3.Exit")
        choice = input("Enter your choice(1-3): ")
        if not os.path.exists("Staff"):
            os.mkdir("Staff")
        if choice == "1":
            while True:
                ID= input("Enter the admin ID: ")
                Password= input("Enter the admin Password: ")
                    # verify Id password from Super.txt
                if super_user_ID == ID and Password == super_user_password:
                        A.Admin()
                        break
                else:
                    print("Admin password wrong")
        elif choice =="2":
            C.customer_login()
        elif choice =="3":
            return
        else:
            print("Enter a valid choice..")
    
    
    
if __name__=="__main__":
    main()
