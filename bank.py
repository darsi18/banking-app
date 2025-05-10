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
def create_customer(customer):
    with open("customer.txt","a")as file:
        file.write(f"{create_customer_next_id()},{customer[0]},{customer[1]},{customer[2]}\n")
        print("customer details saved.")

def create_user(customer):                                                                                                                                                                                               
    with open("users.txt","a")as file:
        file.write(f"{customer[3]},{customer[4]}\n")
        print("user details saved.")

def auto_id():
    try:
        with open("customer.txt","r")as file:
            lines=customer_file.readlines()
            if not lines:
                return"A1"
            last_id_str=lines[-1].split(",")[0]
            last_id_num=int(last_id_str[1:])
            return f"A{last_id_num+1}"
    except FileNotFoundError:
        return"A1"

    def user_login():
        username=input("enter your user name:")
        password=input("enter your password:")
        try:
            with open("user.txt","r")as file:
                for line in file:
                    username,password=line.strip().split(",")
                    if user==username and password==password:
                        print("login successful.")
                        return True
        except FileNotFoundError:
            pass
        print("invalid username and password!")
        return False
    
    def create_auto_id():
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

#transaction history

def store_history(account_number,trasaction_type,amount,new_balance):
    try:
        with open("transaction.txt","a")as file:
            file.write(f"{account_number},{transaction_type},{amount},{new_balance}\n")
    except IOError:
        print("error")

def display_transaction_history(account_number):
    try:
        with open("transaction.txt","r")as file:
            print("\n---transaction history---")
            print("{:<12} {:<10} {:<12}".format("type","amount","balance"))
            print("-"*30)
            found=False
            for line in file:
                data=line.strip().split(",")
                if data[0]==account_number:
                    print("{:<12} {:<10} {:<12}".format(data[1],data[2],data[3]))
                    found=True
            if not found:
                print("no trasaction found!")
    except FileNotFoundError:
        print("trasaction file found!")
    except IOError:
        print("error")

 #trasation bitween 2 accounts

def transfer(sender_account,receiver_account,amount):
    if amount<=0:
        print("transfer amount must be greaterthan zero.")
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
            name,password,account_number,balance=line.strip().split(",")
            balance=float(balance)

            if account_number==sender_account:
                sender_found=True
                if balance<amount:
                print("insufficiant fund in sender accounts!")
                return
            
            sender_balance=balance_amount
            updated_line=f"{name},{password},{account_number},{sender_balance}\n"
            accounts.append(updated_line)
        elif account_number==receiver_account:
            receiver_found=True
            receiver_balance=balance+amount
            updated_line=f"{name},{password},{accoun_number},{receiver_balance}\n"
            amount.append(updated_line)
            else:
            accounts.append(line)
        if not receiver_found:
            print("receicver account is not found!")
            return
        with open("accounts.txt","w")as file:
            file.writelines(accounts)

#store account deatails
        record_transaction(sender_account,"transfer out",amount,sender_balance)
        record_transaction(receiver_account,"trasfer in",amount,receiver_balance)
        print("successfully trasfferd {amount}from{sender_account}to{receiver_account}")
        except FileNotFoundError:
        print("accoun file not found!")
        except IOError:
        print("errorv occurred while accessing the file.")

def user_menu():
    while True:
        print("\n---banking system---")
        print("1.register user")
        print("2.login")
        print("3.exit")
        choice==input("enter your choice:")

        if choice=="1":
            customer=customer_details()
            if customer:
                save_customer(customer)
                save-user(customer)

        elif choice=="2":
            if user_login
                while True
                    print("main menu is here")
                    print("1.create bank account")
                    print("2.deposit money")
                    print("3.withrawal money")
                    print("4.check balance")
                    print('5.transaction history')
                    print("6.transaction bitween two accounts")
                    menu_choice=input("enter your choice")

                    if menu_choice=="1":
                        account_craetion()
                    elif menu_choice=="2":
                        acc_num=input("enter your account number:")
                        try:
                            amt=float(input("enter your deposit amount:"))
                            deposit(acc,amt)
                        except ValueError:
                            print("invalid amount")
                    elif menu_choice=="3":
                       acc_num=input("enter your account number:")
                        try:
                            amt=float(input("enter your withrawal amount:"))
                            withraw(acc,amt)
                        except ValueError:
                            print("invalid amount") 
                    elif menu_choice=="4":
                        check_balance()
                    elif menu_choice=="5":
                        acc_num=input("enter your account number:")
                        display_transaction_history(acc_num)
                    elif menu_choice=="6":
                        sender_account=input("enter the sender's account number:")
                        receiver_account=input("enter the receiver'saccount number:")
                        try:
                            amount=float(input("enter the amount;"))
                            transfer(sender_account,receiver_account,amount)
                        except ValueError:
                            print("invalid amount!")
                        else:
                            print("invalid option")
            elif choice=="3":
                print("thank you")
                break
            else:
                print("invalid choice!")

user_menu()

                                                     




    





    



 

























































































    
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
    










 