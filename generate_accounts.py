import random
import json

def generate_random_pin():
    return f"{random.randint(1000, 9999)}"

def generate_random_balance():
    return random.randint(500, 5000)

# Generate 30 accounts
accounts = {}
for i in range(1, 31):
    user_id = f'user{i}'
    pin = generate_random_pin()
    balance = generate_random_balance()
    accounts[user_id] = {'pin': pin, 'balance': balance, 'history': []}

# Save to account_data.json
with open('account_data.json', 'w') as f:
    json.dump(accounts, f, indent=4)
