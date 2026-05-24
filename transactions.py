# transactions.py — Transaction Engine
from accounts import get_account

def deposit(account_id, amount):
    acc = get_account(account_id)
    if not acc:  # Safety check!
        print(f"Error: Account {account_id} not found.")
        return
        
    acc["balance"] += amount
    acc["history"].append(f"Deposit: +{amount}")
    print(f"Deposited {amount}. Balance: {acc['balance']}")

def withdraw(account_id, amount):
    acc = get_account(account_id)
    if not acc:
        print(f"Error: Account {account_id} not found.")
        return
        
    if acc["balance"] < amount:
        print("Insufficient funds.")
        return
        
    acc["balance"] -= amount
    acc["history"].append(f"Withdrawal: -{amount}")
    print(f"Withdrew {amount}. Balance: {acc['balance']}")

def transfer(from_id, to_id, amount):
    src = get_account(from_id)
    dst = get_account(to_id)
    
    if not src or not dst:
        print("Transfer failed: One or both accounts not found.")
        return
        
    if src["balance"] < amount:
        print("Transfer failed: Insufficient funds.")
        return
        
    src["balance"] -= amount
    dst["balance"] += amount
    src["history"].append(f"Transfer out: -{amount} to {to_id}")
    dst["history"].append(f"Transfer in: +{amount} from {from_id}")
    print(f"Transferred {amount} from {from_id} to {to_id}.")