# reports.py — Reporting Module
from accounts import registry
import copy # Import the copy module

def account_summary(account_id):
    acc = registry[account_id]
    print(f"\n--- Account Summary ---")
    print(f"Owner: {acc['owner']}")
    print(f"Balance: {acc['balance']}")
    print(f"History: {acc['history']}")

def snapshot(account_id):
    acc = registry[account_id]
    # Creates a full, independent copy including the nested history list
    snap = copy.deepcopy(acc) 
    return snap

def audit_report():
    print("\n=== Audit Report ===")
    for acc_id, acc in registry.items():
        print(f"{acc_id}: {acc['owner']} | Balance: {acc['balance']}")