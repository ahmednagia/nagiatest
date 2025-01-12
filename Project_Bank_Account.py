import os
import random

class BankAccount:
    def __init__(self, name, account_type, balance=0):
        # Initialize the account with basic details
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.account_id = self.generate_account_id()  # Unique account ID
        self.transaction_history = []
        
        # File name for storing transaction history
        self.statement_file = f"{self.name}_{self.account_type}_{self.account_id}.txt"
        
        # Create a new file for storing transaction history
        self.create_transaction_file()
        
        print(f"Account created for {self.name} with ID {self.account_id} in {self.account_type} account.")
    
    def generate_account_id(self):
        # Generate a random 6-digit account ID
        return random.randint(100000, 999999)
    
    def create_transaction_file(self):
        # Create a new file with the initial balance information
        if not os.path.exists(self.statement_file):
            with open(self.statement_file, 'w') as file:
                file.write(f"Account created for {self.name}\nAccount Type: {self.account_type}\nInitial Balance: {self.balance}\n")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            transaction = f"Deposited: ${amount} | New Balance: ${self.balance}"
            self.transaction_history.append(transaction)
            self.record_transaction(transaction)
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            transaction = f"Withdrew: ${amount} | New Balance: ${self.balance}"
            self.transaction_history.append(transaction)
            self.record_transaction(transaction)
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    
    def get_balance(self):
        return self.balance
    
    def get_account_id(self):
        return self.account_id
    
    def get_username(self):
        return self.name
    
    def get_account_type(self):
        return self.account_type
    
    def record_transaction(self, transaction):
        # Write transaction to the file
        with open(self.statement_file, 'a') as file:
            file.write(transaction + "\n")
    
    def get_transaction_history(self):
        # Read transaction history from the file
        with open(self.statement_file, 'r') as file:
            history = file.readlines()
            print("Transaction History:")
            for line in history:
                print(line.strip())
            return history

# Test the BankAccount class with multiple objects and transactions
def main():
    # Creating two bank accounts for testing
    account1 = BankAccount("JohnDoe", "savings")
    account2 = BankAccount("JaneSmith", "chequing")
    
    # Performing some transactions on account1
    account1.deposit(500)
    account1.withdraw(200)
    account1.get_transaction_history()
    
    # Performing some transactions on account2
    account2.deposit(1000)
    account2.withdraw(150)
    account2.get_transaction_history()
    
    # Checking balances and account info
    print(f"{account1.get_username()}'s Balance: ${account1.get_balance()}")
    print(f"{account2.get_username()}'s Balance: ${account2.get_balance()}")

# Running the test
if __name__ == "__main__":
    main()
