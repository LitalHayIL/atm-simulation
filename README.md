### README


# Advanced ATM Simulator

## Overview

This Python program simulates an ATM with advanced features. Users can:
- Check their balance
- Withdraw money
- Deposit money
- View their transaction history

## Features

- **Account Management:** Multiple users with unique PINs and balances.
- **Transaction History:** Records and displays all transactions with timestamps.
- **Error Handling:** Handles invalid inputs and transactions gracefully.
- **Transaction Limits:** Ensures withdrawal and deposit amounts are positive and within balance constraints.

## Requirements

- Python 3.x

## Generate dummy account data
#Run the Script
Save the above code to a file, say generate_accounts.py, and run it with:

 ```bash
python generate_accounts.py
 ```
This will create an account_data.py file with 30 different accounts.

Resulting account_data.py
The account_data.py file will look something like this:

 ```bash
accounts = {
    "user1": {"pin": "1234", "balance": 2567, "history": []},
    "user2": {"pin": "5678", "balance": 4380, "history": []},
    "user3": {"pin": "9101", "balance": 2123, "history": []},
    # Add 27 more accounts here...
    "user30": {"pin": "6789", "balance": 4790, "history": []}
}
 ```
Each account will have a unique user_id, a randomly generated pin, and a randomly assigned balance between 500 and 5000. You can adjust the balance range or the number of accounts as needed.

## Usage

1. **Run the Program:**
   ```bash
   python atm_simulator.py
   ```

2. **Enter User ID:**
   The program will prompt for a user ID. Enter either `user1` or `user2`.

3. **Enter PIN:**
   Enter the correct PIN associated with the user ID.

4. **Select Menu Option:**
   - **1:** Check balance
   - **2:** Withdraw money
   - **3:** Deposit money
   - **4:** View transaction history
   - **5:** Exit the program

## Example

```bash
Welcome to the Advanced ATM Simulator
Enter your user ID (user1/user2): user1
Please enter your PIN: 1234
PIN is correct.
Menu:
1. Check balance
2. Withdraw money
3. Deposit money
4. View transaction history
5. Exit
Choose an option (1-5): 2
How much do you want to withdraw? 150
Successfully withdrew $150.
Your new balance is $850
```
