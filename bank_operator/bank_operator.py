from account.user import User
from account.bank_account import BankAccount, SavingsAccount, CurrentAccount, StudentAccount

users = []

def create_user():
    name = input("Enter name: ")
    email = input("Enter email: ")
    user = User(name, email)
    if not user.is_valid_email(email):
        print("Invalid email address!")
        return
    users.append(user)
    print(f"User {name} created.\n")

def list_users():
    if not users:
        print("No users available. Please create a user first.\n")
        return False
    for i, user in enumerate(users):
        print(f"{i+1}. {user}")
    return True

def create_account():
    if not list_users():
        return
    try:
        idx = int(input("Select user number: ")) - 1
        if idx not in range(len(users)):
            print("Invalid user selection.\n")
            return
        print("Account Type:")
        print("1. Savings Account")
        print("2. Students Account")
        print("3. Current Account")
        account_choice = int(input("Enter your choice (1, 2, 3): "))
        amount = float(input("Enter initial deposit: "))

        if account_choice == 1:
            account = SavingsAccount(users[idx].name, users[idx].email, amount)
        elif account_choice == 2:
            account = StudentAccount(users[idx].name, users[idx].email, amount)
        elif account_choice == 3:
            account = CurrentAccount(users[idx].name, users[idx].email, amount)
        else:
            print("Invalid account type!")
            return

        users[idx].add_account(account)
        print(f"{account.get_account_type()} added!\n")
    except (ValueError, IndexError):
        print("Invalid input or operation.\n")

def deposit_money():
    if not list_users():
        return
    try:
        idx = int(input("Select user: ")) - 1
        if idx not in range(len(users)):
            print("Invalid user selection.\n")
            return
        user = users[idx]
        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
        acc_idx = int(input("Select account: ")) - 1
        amount = float(input("Enter amount to deposit: "))
        user.accounts[acc_idx].deposit(amount)
    except (ValueError, IndexError):
        print("Invalid input.\n")

def withdraw_money():
    if not list_users():
        return
    try:
        idx = int(input("Select user: ")) - 1
        if idx not in range(len(users)):
            print("Invalid user selection.\n")
            return
        user = users[idx]
        for i, acc in enumerate(user.accounts):
            print(f"{i+1}. Balance: Rs. {acc.get_balance()}")
        acc_idx = int(input("Select account: ")) - 1
        amount = float(input("Enter amount to withdraw: "))
        user.accounts[acc_idx].withdraw(amount)
        print("Withdrawal successful.\n")
    except (ValueError, IndexError):
        print("Error during withdrawal.\n")

def view_transactions():
    if not list_users():
        return
    try:
        idx = int(input("Select user: ")) - 1
        if idx not in range(len(users)):
            print("Invalid user selection.\n")
            return
        user = users[idx]
        for i, acc in enumerate(user.accounts):
            print(f"\n{acc.get_account_type()} {i+1} - Balance: Rs. {acc.get_balance()}")
            for tx in acc.get_transaction_history():
                print(tx)
    except (ValueError, IndexError):
        print("Invalid input.\n")
