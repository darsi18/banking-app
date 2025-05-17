import os

#get customer details
def customer_details():
    customer_name=input("Enter Your Name:")
    customer_address=input("Enter Your Address:")
    customer_username=input("Enter Your user Name:")
    return[customer_name,customer_address,customer_username]
customer_details()

#password length
def password_check():
    while True:
        customer_password=input("Enter your password(minimum six characters):")
        if len(customer_password)>=6:
            print("your password is correct")
        else:
            print("please enter must be six characters!")
        return[customer_password]
password_check()

'''
#change password
def change_password(username,customer):
    try:
        with open("users.txt","r")as file:
            for line in file:
'''

#store data as a customer file
def create_customer(customer):
    with open("customer.txt","a")as file:
        file.write(f"{auto_id()},{customer[0]},{customer[1]},\n")
        print("Customer details successfully saved.")

#store data as a user file
def create_user(customer):                                                                                                                                                                                               
    with open("users.txt","a")as file:
        file.write(f"{customer[2]},{customer[3]},{customer[4]}\n")
        print("User details successfully saved.")

#check admin status
def admin_status(customer_username):
    customer_password=input("enter your password:")
    with open("user.txt","r") as file:
        for line in file:
            user,pwd=line.strip().split(",")
            if customer_username==user and customer_password==pwd:
                print("your a admin")
            else:
                print("you are a customer")
admin_status()

#create auto generate account number
def auto_id():
    try:
        with open("customer.txt","r")as customer_file:
            lines=customer_file.readlines()
            if not lines:
                return"A1"
            last_id_str=lines[-1].split(",")[0]
            last_id_num=int(last_id_str[1:])
            return f"A{last_id_num+1}"
    except FileNotFoundError:
        return"A1"

#login the accounts
def user_login():
        username=input("Enter your user name:")
        password=input("Enter your password:")
        try:
            with open("users.txt","r")as file:
                for line in file:
                    user,pwd=line.strip().split(",")
                    if username==user and password==pwd:
                        print("login successful.")
                        return True
        except FileNotFoundError:
            pass
        print("login failed! please try again later!.")
        return False

#create account
def account_creation():
    account_number=input("Enter your account number:")
    name=input("Enter your holder name:")
    balance=float(input("Enter your initial balance:"))
    if balance < 0:
        print(f"initial balance must be greaterthan zero.")
        return
    with open("accounts.txt","a")as file:
        file.write(f"{account_number},{name},{balance}\n") 
        print(f"account sucessfully creted.your account number is:{account_number}")

#deposit money
def deposit_money(acc_number,amount):
    if amount<=0:
        print("Amount must be greater than zero!")
        return
    try:
        accounts=[]
        account_found = False

        with open("accounts.txt","r")as file:
            for line in file:
                account_number,name,balance=line.strip().split(",")
                if acc_number==account_number:
                    account_found=True
                    new_balance=float(balance)+amount
                    print(f"successfully deposited {amount}.New balance is: {new_balance}")

                    line=f"{account_number},{name},{new_balance}\n"   
                    accounts.append(line)

                    store_history(acc_number,"deposit",amount,new_balance) 
                else: 
                    accounts.append(line)

        if not account_found:
            print("Account is not found.")

        with open("accounts.txt","w")  as file:
            file.writelines(accounts)
    except FileNotFoundError:
        print("Accounts file is not found!")
    except IOError:
        print("An error occurated while reading or writing to the file!")

#withdraw money
def withdraw_money(acc_number,amount):
    if amount<=0:
        print("Enter the amount must be greater than zero!")
        return
    
    try:
        account_found = False
        accounts=[]

        with open("accounts.txt","r")as file:
            for line in file:
                account_number,name,balance=line.strip().split(",")
                if acc_number==account_number:
                    account_found=True
                    balance=float(balance)
                    if amount>balance:
                        print("insufficiant funds.")
                        return
                    else:
                        balance-=amount
                        print(f"successfully withrawal amount{amount}.new balance is:{balance}.")
                        line=f"{name},{account_number},{balance}\n"
                        store_history(account_number,"withdraw",amount,balance)
                        accounts.append(line)
                else:
                    accounts.append(line)
    except FileNotFoundError:
        print("Account file is not found!")
        return
    if not account_found:
        print("Account is not found!")
        return
    try:
        with open("accounts.txt","W")as file:
            file.writelines(accounts)
    except IOError:
        print("Error! Try Again.")

#check the balance
def check_balance():
    account_number=input("Enter your account number:")
    try:
        with open("accounts.txt","r")as file:
            for line in file:
                account_number,name,balance=line.strip().split(",")
                if account_number==account_number:
                    print(f"account balance is:{balance}")
                    return
        print("Account not found.")
    except FileNotFoundError:
        print("Account file not error")
    except IOError:
        print("Error! Try Again.")

#transaction history

def store_history(account_number,transaction_type,amount,new_balance):
    try:
        with open("transaction.txt","a")as file:
            file.write(f"{account_number},deposit,{amount},{new_balance}\n")
    except IOError:
        print("Error! Try Again.")

def display_transaction_history(account_number):
    try:
        with open("transaction.txt","r")as file:
            print("\n---Transaction History Is Here---")
            print("{:<12} {:<10} {:<12}".format("type","amount","balance"))
            print("-"*30)
            found=False
            for line in file:
                data=line.strip().split(",")
                if data[0]==account_number:
                    print("{:<12} {:<10} {:<12}".format(data[1],data[2],data[3]))
                    found=True
            if not found:
                print("No trasaction found!")
    except FileNotFoundError:
        print("Trasaction file is not found!")
    except IOError:
        print("Error! Try Again.")

 #trasation bitween 2 accounts

def transfer(sender_account,receiver_account,amount):
    if amount<=0:
        print("Transfer amount must be greaterthan zero!")
        return
    try:
        accounts=[]
        sender_found=False
        receiver_found=False
        sender_balance=0.0
        receiver_balance=0.0

#store all accounts

        with open("accounts.txt","r")as file:
            for line in file:
                account_number,name,balance=line.strip().split(",")
                balance=float(balance)

            if account_number==sender_account:
                sender_found=True
                if balance<amount:
                    print("Insufficiant fund in sender accounts!")
                    return
            
                sender_balance=balance-amount
                updated_line=f"{name},{account_number},{sender_balance}\n"
                accounts.append(updated_line)
            elif account_number==receiver_account:
                receiver_found=True
                receiver_balance=balance+amount
                updated_line=f"{name},{account_number},{receiver_balance}\n"
                accounts.append(updated_line)
            #else:
               # accounts.append(line)
        if not receiver_found:
            print("Receicver account is not found!")
            return
        with open("accounts.txt","w")as file:
            file.writelines(accounts)

#store account deatails
            display_transaction_history(sender_account,"transfer out",amount,sender_balance)
            display_transaction_history(receiver_account,"transfer in",amount,receiver_balance)
            print("successfully transfferd {amount}from{sender_account}to{receiver_account}")

    except FileNotFoundError:
            print("Account file not found!")
        
    except IOError:
            print("Error occurred while accessing the file!")

def user_menu():
    while True:
        print("\n---banking Options Are Here---")
        print("1.Register User")
        print("2.Login")
        choice = input("Enter your choice:")

        if choice=="1":
            customer=customer_details()
            if customer:
                create_customer(customer)
                create_user(customer)

        elif choice=="2":
            if user_login():
                while True:
                    print("\n---Main Menu Is Here---")
                    print("1.Create bank account")
                    print("2.Deposit Money")
                    print("3.Withrawal Money")
                    print("4.Check Balance")
                    print('5.Transaction History')
                    print("6.Transaction bitween two accounts")
                    print("7.display customer list")
                    print("8.check admin ststus")
                    print("9.Exit")
                  
                    user_option=input("Enter your choice:")

                    if user_option=="1":
                        account_creation()
                    elif user_option=="2":
                        acc_number=input("Enter your account number:")
                        try:
                            amt=float(input("Enter your deposit amount:"))
                            deposit_money(acc_number,amt)
                        except ValueError:
                            print("Successfully Deposited.")
                    elif user_option=="3":
                        acc_number=input("Enter your account number:")
                        try:
                            amt=float(input("Enter your withrawal amount:"))
                            withdraw_money(acc_number,amt)
                        except ValueError:
                            print("Successfully withdrawal")
                        
                    elif user_option=="4":
                        check_balance()
                    elif user_option=="5":
                        acc_num=input("Enter your account number:")
                        display_transaction_history(acc_num)
                    elif user_option=="6":
                        sender_account=input("Enter the sender's account number:")
                        receiver_account=input("Enter the receiver'saccount number:")
                        try:
                            amount=float(input("Enter the amount:"))
                            transfer(sender_account,receiver_account,amount)
                        except ValueError:
                            print("Invalid amount:")
                        else:
                            print("Invalid option")
                    elif user_option=="7":
                        customer_details()
                    elif user_option=="8":
                        admin_status()
                    elif user_option=="9":
                            print("\n---Thank you for using our bank---")
                            break
                    else:
                        print("Invalid choice please try again!")

user_menu()
    










 