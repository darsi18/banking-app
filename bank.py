
def customer_info():
    customer_name=input("enter your number:")
    customer_address=input("enter your address:")
    customer_nic_no=int(input("enter your nic mumber"))
    customer_phone_number=int(input("enter your phone number"))
customer_info()

user_name="darsi"
pass_word="1234"

maxattempts=3
attempts=0

while attempts < maxattempts:
    username=input("enter your user name:")
    password=input("enter your password:")
if username==user_name and password==pass_word:
    print("your succussfully signin the account.")
break
else:
  attempts+=1
  remaining = maxattempts-attempts
  print(f"one time left")
if attempts==maxattempts:
   print("too many failed attempts.exiting program.")

accounts={}
next_account_number=111

def account_creation():
    global next_account_number
    name=input("enter your holder name:")
    balance=float(input("enter your initial balance:"))
    if initial_balance < 0:
        print("initial balance must be non_negative!")
        return
    
    account_number=int(next_account_number)
    next_acount_number +=1
    accounts[account_number]={'name':'name','balance':float(balance),'transaction':[f"account created with balance{balance}"]}
    print(f"account sucessfully creted.your account number is:{account_number}")

def deposit_money():
    acc_no=input("enter your account number:")
    if acc_no not in accounts:
        print("accounts is not found.")
        return
    amount=float(input("enter your deposit amount:"))
    if amount<=0:
        print("your deposit amount must be positive!")
        return
    account[acc_no]['balance']+=amount
    accounts[acc_no]['trasaction'].append(f"deposited{amount}")
    print("deposited successfully.")

def withdraw_money():
    acc_no=input("enter your account number:")
    if acc_no not in accounts:
        print("accounts is not found.")
        return
    amount=float(input("enter your withdraw amount:"))
    if amount<=0:
        print("your withdraw amount must be positive!")
        return
    if amount>accounts[acc_no]['balance']:
        print("insufficiant balance.")
        return
    account[acc_no]['balance']-=amount
    accounts[acc_no]['trasaction'].append(f"withdraw{amount}")
    print("withdrawal successfully.")

def check_balance():
    acc_no=input("enter your account number:")
    if acc_no not in accounts:
        print("account not found!")
        return
    print(f"current balance:{accounts[acc_no]['balance']}")

def transaction_history():
    acc_no=input("enter your account number:")
    if acc_no not in accounts:
        print("account not found!")
        return
    print("transaction history:")
    for trasaction in accounts[acc_no]['transaction']:
        print(transaction)

def menu():
    while true:
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
        if choice=='2':
            deposit_money()
        if choice=='3':
            withdraw_money()
        if choice=='4':
            (check_balance)
        if choice=='5':
            (transactiom_history)
        if choice=='6':
            ("exiting")
        break 
    else:
        ("thank you.")

    










 