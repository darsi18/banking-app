user_name="darsi"
pass_word="1234"

maxattempts=3
attempts=0

while attempts < maxattempts:
    username=input("enter your user name:")
    password=input("enter your password:")

if username==user_name and password==pass_word:
    print("your succussfully signin the account.")
else:
  attempts=attempts+1
  remaining = maxattempts-attempts
  print(f"one time left")

if attempts==maxattempts:
   print("too many failed attempts.exiting program.")

accounts={}
next_account_number=111