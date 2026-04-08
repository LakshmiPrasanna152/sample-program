# Simple Bank Account System


class BankAccount:
    """
    ABSTRACTION: User only sees deposit, withdraw, get_balance.
    They don't need to know HOW money is stored or validated internally.
    """

    def __init__(self, owner, balance=0):
        self.owner = owner                  
        self.__balance = balance            
        self.__transactions = []          

    # ENCAPSULATION: Private method — internal use only
    def __record_transaction(self, type, amount):
        self.__transactions.append(f"{type}: ₹{amount}")

    # ABSTRACTION: Simple interface to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__record_transaction("Deposit", amount)
            print(f"✅ Deposited ₹{amount}. New Balance: ₹{self.__balance}")
        else:
            print("❌ Invalid deposit amount!")

    # ABSTRACTION: Simple interface to withdraw money
    def withdraw(self, amount):
        if amount > self.__balance:
            print("❌ Insufficient funds!")
        elif amount <= 0:
            print("❌ Invalid withdrawal amount!")
        else:
            self.__balance -= amount
            self.__record_transaction("Withdraw", amount)
            print(f"✅ Withdrew ₹{amount}. New Balance: ₹{self.__balance}")

    # ENCAPSULATION: Controlled access to private balance
    def get_balance(self):
        return self.__balance

    # ABSTRACTION: User just calls this to see history
    def show_summary(self):
        print(f"\n📋 Account Summary for {self.owner}")
        print(f"   Balance: ₹{self.__balance}")
        print(f"   Transactions: {self.__transactions}")


# ──────────────────────────────────────────
# OBJECT: Creating instances of BankAccount
# ──────────────────────────────────────────
account1 = BankAccount("Alice", 1000)   # Object 1
account2 = BankAccount("Bob", 500)      # Object 2

print("=== Alice's Transactions ===")
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(5000)   # Should fail

print("\n=== Bob's Transactions ===")
account2.deposit(300)
account2.withdraw(100)

# Show summaries
account1.show_summary()
account2.show_summary()

# Trying to access private variable directly → will FAIL (Encapsulation working!)
# print(account1.__balance)  # ❌ AttributeError: can't access private variable
print("\n✅ Direct access to __balance is blocked (Encapsulation)!")