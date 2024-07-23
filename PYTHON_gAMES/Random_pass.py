import string
import random

smallcase = string.ascii_lowercase
uppcase = string.ascii_uppercase
digits = string.digits
symbol = string.punctuation
print("\n===== Welcome To Password Generator ======\n")

while True:
    try:
        user_pass = ""
        fullstr = ""
        length = int(input("Enter the lenght you want your password: "))
        include_uppercase = input("Would you like to have upper case in your password (y/n): ").upper()
        include_low = input("Would you like to have lower  in your password (y/n): ").upper()
        include_udig = input("Would you like to have digits in your password (y/n): ").upper()
        include_symbol = input("Would you like to have symbol in your password (y/n): ").upper()

        if include_uppercase == "Y":
            fullstr += uppcase

        if include_low =="Y":
            fullstr+=smallcase

        if include_symbol == "Y":
            fullstr+=symbol

        if include_udig == "Y":
            fullstr+=digits

        new_pass = random.sample(fullstr , length) # automatically suffle the string and give the req lenght string
        for i in new_pass:
            user_pass+=i

        print("\n====== Your Password ========")
        print("Your password =",user_pass)
        print("==========================")
        
    except ValueError :
        print("Enter valid choice.")