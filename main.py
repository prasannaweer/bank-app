# main.py — Entry point
from accounts import create_account
from transactions import deposit, withdraw, transfer
from reports import account_summary, audit_report, snapshot

print("--- INITIALIZING ACCOUNTS ---")
create_account("ACC001", "Nimal Perera", 1000)
create_account("ACC002", "Amali Silva", 500)
create_account("ACC003", "Kamal Fernando", 750)  

print("\n--- PROCESSING TRANSACTIONS ---")
# Let's test the transaction engine
deposit("ACC001", 200)
withdraw("ACC002", 100)
transfer("ACC003", "ACC002", 250)

print("\n--- GENERATING REPORTS ---")
# See the history update
account_summary("ACC002")

# View the whole system
audit_report()

# Test if our snapshot bug is fixed
print("\n--- TESTING SNAPSHOT ---")
my_snap = snapshot("ACC001")
my_snap["balance"] = 9999999  # Attempting to tamper with the snapshot
print(f"Snapshot balance: {my_snap['balance']}")

# Check the live registry to ensure the real account wasn't affected
actual_account = account_summary("ACC001")