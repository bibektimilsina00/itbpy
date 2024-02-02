import json
import os






# File to store data
data_file = 'bank_data.json'

def read_data():
    if not os.path.exists(data_file):
        return {}
    
    with open(data_file, 'r') as file:
        return json.load(file)

def write_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)





def create_account():

    users = read_data()
    users={}
    username = input("Enter a new username: ")

    if username in users:
        print("Username already exists.")
        return
    
    password = input("Enter a new password: ")

    users[username] = {'password': password, 'balance': 0}

 

 
    write_data(users)
    print("Account created successfully!")

def login():

    users = read_data()
    username = input("Enter your username: ")
    password = input("Enter your password: ")


    
    if username in users and users[username]['password'] == password:
        return username
    else:
        print("Invalid username or password.")
        return None

def deposit(user):
    amount = float(input("Enter amount to deposit: "))
    users = read_data()
    users[user]['balance'] += amount



 

    write_data(users)


    print(f"Deposited {amount}. New balance: {users[user]['balance']}")

def withdraw(user):
    
    amount = float(input("Enter amount to withdraw: "))
    users = read_data()
    
    if amount <= users[user]['balance']    :
        users[user]['balance'] -= amount
        write_data(users)
        print(f"Withdrew {amount}. New balance: {users[user]['balance']}")
    else:
        print("Insufficient balance.")

def check_balance(user):
    users = read_data()
    print(f"Current balance: {users[user]['balance']}")







def main():



    while True:
        print("\n--- ItBridge Banking System ---")
        print("1. Create a new account")
        print("2. Access existing account")
        print("3. Exit")
        choice = input("Enter your choice: ")




        if choice == '1':
            create_account()
        elif choice == '2':
            user = login()

            
            if user:
                while True:

                    print("\n--- Account Menu ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")
                    account_choice = input("Enter your choice: ")

                    if account_choice == '1':
                        deposit(user)
                    elif account_choice == '2':
                        withdraw(user)
                    elif account_choice == '3':
                        check_balance(user)
                    elif account_choice == '4':
                        break
        elif choice == '3':
            break



main()