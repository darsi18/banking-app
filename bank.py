import os
#get customer details
def customer_details():
    customer_name=input("enter your name:")
    customer_address=input("enter your address:")
    customer_nic_no=int(input("enter your nic mumber:"))
    customer_username=input("enter your user name:")
    customer_password=input("enter your password:")
    return[customer_name,customer_address,customer_nic_no,customer_username,customer_password]
customer_details()

#store customer & user details
def create_customer():
    customers=customer_details()
    with open("customer.txt","a")as file:
        file.write(f"{customers[0]},{customers[2]}\n")

def create_user():
    customers=customer_details()                                                                                                                                                                                                
    with open("users.txt","a")as file:
        file.write(f"{customers[3]},{customers[4]}\n")

def auto_id():
    with open("users.txt","r")as user_file:
        user_id=user_file.readlines()[-1].split(",")[0]
        characters=list(user_id)

def create_auto_id():
    try:
        with open("customer.txt","r")as customer_file:
            lines=customer_file.readlines()
            if not lines:
                return"a1"
            last_id_str=lines[-1].split(",")[0]
            last_id_num=int(last_id_str[1:])
            return f"a{last_id_num+1}"
    except FileNotFoundError:
            return"a1"

def account_creation():
    accounts=[]
    account_found=False
    account_number=input("enter your account number:")
    name=input("enter your holder name:")
    balance=float(input("enter your initial balance:"))
    if balance < 0:
        print(f"initial balance must be greaterthan zero.")
        return
    with open("accounts.txt","a")as file:
        file.write(f"{account_number},{name},{balance}")
        print(f"account sucessfully creted.your account number is:{account_number}")

def deposit_money(account_number,amount):
    if amount<=0:
        print("amount must be greaterv than zero!")
        return
    try:
        account_found = False
        accounts=[]

        with open("accounts.txt","r")as file:
            for line in file:
                name,password,account_number=line.strip().split(",")
                if account_number==account_number:
                    account_found=True
                    new_balance=float(balance)+amount
                    print(f"successfully deposited {amount}.New balance is: {new_balance}")

                    line=f"{account_number};{name};{new_balance}\n"   
                    accounts.append(line)

                    accounts(account_number,"deposit",amount,new_balance) 
                else: 
                    accounts.append(line)

        if not account_found:
            print("account is not found.")

        with open("accounts.txt","w")  as file:
            file.writelines(accounts)
    except IOError:
        print("error")


def withdraw_money():
    if amount<=0:
        print("enter the amount must be greater than zero!")
        return
    
    try:
        account_found = False
        accounts=[]

        with open("accounts.txt","r")as file:
            for line in file:
                name,password,account_number=line.strip().split(",")
                if account_number==account_number:
                    account_found=True
                    new_balance=float(balance)
                    if amount>balance:
                        print("insufficiant funds.")
                        return
                    else:
                        balance-=amount
                        print(f"successfully withrawal amount{amoun}.new balance is:{balance}.")
                        line=f"{name},{password},{acc_number},{balance}\n"
                        record_transaction(account_number,"withdraw",amount,balance)
                        accounts.append(line)
                else:
                    accounts.append(line)
    except FileNotFoundError:
        print("account file is not found!")
        return
    if not account_found:
        print("account not found")
        return
    try:
        with open("accounts.txt","W")as file:
            file.writelines(accounts)
    except IOError:
        print("error")


def check_balance():
    acc_no=input("enter your account number:")
    try:
        with open("accounts.txt","r")as file:
            for line in file:
                name,password,account_number,balance=line.strip().split(",")
                if acc_number==account_number:
                    print(f"account balance is:"{balance}"")
                    return
        print("account not found.")
    except FileNotFounderror:
        print("account file not error")
    except IOError:
        print("error")
    
    #trasation history


















    
def menu():
    while True:
        print("\n mini banking system")
        print("1.create account")
        print("2.deposit money")
        print("3.withdraw money")
        print("4.check balance")
        print("5.transcation history")
        print("6.exit")

        choice=input("enter your choice:")

        if choice=='1':
            account_creation()
        elif choice=='2':
            deposit_money()
        elif choice=='3':
            withdraw_money()
        elif choice=='4':
            (check_balance)
        elif choice=='5':
            (transactiom_history)
        elif choice=='6':
            ("exiting")
            break 
        else:
         ("thank you.")
menu()
    










 