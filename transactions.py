# transactions.py — Transaction Engine
from accounts import registry

def deposit(account_id, amount):
    if account_id not in registry:
        print(f"Error: Account {account_id} not found.")
        return
        
    acc = registry[account_id]
    if acc["frozen"]:
        print(f"Transaction Denied: Account {account_id} is frozen.")
        return

    acc["balance"] += amount
    acc["history"].append(f"Deposited: +{amount}")
    print(f"Deposited {amount} into {account_id}. New Balance: {acc['balance']}")


def withdraw(account_id, amount):
    if account_id not in registry:
        print(f"Error: Account {account_id} not found.")
        return
        
    acc = registry[account_id]
    if acc["frozen"]:
        print(f"Transaction Denied: Account {account_id} is frozen.")
        return
        
    if acc["balance"] < amount:
        print(f"Transaction Denied: Insufficient funds in {account_id}.")
        return

    acc["balance"] -= amount
    acc["history"].append(f"Withdrew: -{amount}")
    print(f"Withdrew {amount} from {account_id}. New Balance: {acc['balance']}")


def transfer(from_id, to_id, amount):
    if from_id not in registry or to_id not in registry:
        print("Error: One or both account IDs do not exist.")
        return
        
    src = registry[from_id]
    dst = registry[to_id]
    
    if src["frozen"] or dst["frozen"]:
        print("Transaction Denied: One or both accounts are frozen.")
        return
        
    if src["balance"] < amount:
        print(f"Transaction Denied: Insufficient funds in {from_id} to transfer.")
        return

    src["balance"] -= amount
    dst["balance"] += amount
    
    src["history"].append(f"Transfer out: -{amount} to {to_id}")
    dst["history"].append(f"Transfer in: +{amount} from {from_id}")
    print(f"Transferred {amount} from {from_id} to {to_id}.")


def freeze_account(account_id):
    """Standalone function to freeze accounts."""
    if account_id not in registry:
        print(f"Error: Account {account_id} not found.")
        return
        
    acc = registry[account_id]
    acc["frozen"] = True
    acc["history"].append("Account frozen.")
    print(f"Account {account_id} frozen")