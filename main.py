import mysql.connector
connection = mysql.connector.connect(user = "root", database = "Base", password =  "Speedcoder15")
cursor = connection.cursor()
testQuery = ("SELECT * FROM Account")
cursor.execute(testQuery)

 for item in cursor:
     print(item)
 cursor.close()
 connection.close()

def balance():  
    balance = (sum)


def home_screen(): 
    print(f"Welcome {user_name}")
    print(f'balance =  {sum}')
    user_selection()

def deposit():
      deposit = input("insert value ") 
      #fetch  balance in account
      float(sum)+float(deposit) = balance()
      print('{balance} = (sum)')

def withdraw():
    withdraw = input("insert value ")
    float(sum)-float(withdraw)
    print("balance = (sum)")

home_screen()

def user_selection():
  selection = int(input("Select a option, deposit or withdraw: "))
  if selection == deposit:
     print("Initiating Deposit")
     deposit()
  elif selection == withdraw:
     print("Initiating Withdraw")
     withdraw()
