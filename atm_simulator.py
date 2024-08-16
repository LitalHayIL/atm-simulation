import datetime
import json
import os

# File to store account data
ACCOUNT_FILE = 'account_data.json'

def load_accounts():
    if os.path.exists(ACCOUNT_FILE):
        with open(ACCOUNT_FILE, 'r') as f:
            return json.load(f)
    else:
        # Initialize accounts if the file does not exist
        return {
            f'user{i}': {'pin': f'{1000 + i}', 'balance': 1000 + i * 100, 'history': []}
            for i in range(1, 31)
        }

def save_accounts(accounts):
    with open(ACCOUNT_FILE, 'w') as f:
        json.dump(accounts, f, indent=4)

def print_transaction_history(account):
    print("\nTransaction History:")
    for entry in account['history']:
        print(entry)
    print()

def update_transaction_history(account, action, amount):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} - {action}: ${amount}"
    account['history'].append(entry)

def atm_menu():
    print("Menu:")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Deposit money")
    print("4. View transaction history")
    print("5. Exit")

def main():
    print("Welcome to the Advanced ATM Simulator")

    # Load account data
    accounts = load_accounts()

    user_id = input("Enter your user ID (user1/user2/.../user30): ").strip()
    if user_id not in accounts:
        print("Invalid user ID.")
        return

    correct_pin = accounts[user_id]['pin']
    atm_on = False

    while not atm_on:
        user_pin = input("Please enter your PIN: ").strip()
        if user_pin == correct_pin:
            print("PIN is correct.")
            atm_on = True
        else:
            print("Incorrect PIN. Please try again.")

    while atm_on:
        atm_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            print(f"Your balance is ${accounts[user_id]['balance']}\n")

        elif choice == '2':
            withdraw_amount = input("How much do you want to withdraw? ").strip()
            try:
                withdraw_amount = int(withdraw_amount)
                if withdraw_amount <= 0:
                    print("Withdrawal amount must be positive.")
                elif withdraw_amount > accounts[user_id]['balance']:
                    print("Insufficient balance.")
                else:
                    accounts[user_id]['balance'] -= withdraw_amount
                    update_transaction_history(accounts[user_id], "Withdraw", withdraw_amount)
                    print(f"Successfully withdrew ${withdraw_amount}.")
                    print(f"Your new balance is ${accounts[user_id]['balance']}\n")
                    save_accounts(accounts)  # Save the updated data
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '3':
            deposit_amount = input("How much do you want to deposit? ").strip()
            try:
                deposit_amount = int(deposit_amount)
                if deposit_amount <= 0:
                    print("Deposit amount must be positive.")
                else:
                    accounts[user_id]['balance'] += deposit_amount
                    update_transaction_history(accounts[user_id], "Deposit", deposit_amount)
                    print(f"Successfully deposited ${deposit_amount}.")
                    print(f"Your new balance is ${accounts[user_id]['balance']}\n")
                    save_accounts(accounts)  # Save the updated data
            except ValueError:
                print("Invalid amount. Please enter a number.")

        elif choice == '4':
            print_transaction_history(accounts[user_id])

        elif choice == '5':
            print("Exiting the menu. Goodbye!")
            atm_on = False

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
