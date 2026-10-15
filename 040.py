# Problem 040: ATM Withdrawal : Approve or reject a withdrawal based on amount, balance, and minimum-balance rules.

# Rules used:
# 1. Amount must be a multiple of 100
# 2. Amount must not be more than the balance
# 3. After withdrawal, at least Rs. 500 (minimum balance) must remain
min_balance = 500

balance = float(input("Enter account balance: "))
amount = float(input("Enter amount to withdraw: "))

if amount <= 0:
    print("Rejected: Invalid amount")
elif amount % 100 != 0:
    print("Rejected: Amount must be a multiple of 100")
elif amount > balance:
    print("Rejected: Insufficient balance")
elif balance - amount < min_balance:
    print("Rejected: Minimum balance of", min_balance, "must be maintained")
else:
    print("Approved. Remaining balance:", balance - amount)
