class BankAccount:
    counter = 1000

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0
        BankAccount.counter += 1
        self.account_number = BankAccount.counter

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print(self.account_holder, "Balance:", self.balance)

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print("Transfer successful!")
        else:
            print("Insufficient balance for transfer!")


# Create two bank accounts
a1 = BankAccount("Rahul")
a2 = BankAccount("Priya")

# Perform operations
a1.deposit(5000)
a1.withdraw(1000)
a1.transfer(2000, a2)

# Display balances
a1.display_balance()
a2.display_balance()
