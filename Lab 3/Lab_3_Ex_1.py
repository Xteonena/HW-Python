class bank_account:

    def __init__(self, account_number, name, balance, password):
        self.account_number = account_number
        self.accountNumber = account_number
        self.name = name
        self.balance = balance
        self.password = password

    def deposit(self, amount):
        self.balance += amount
        print("Amount", amount, "has been successfully credited to your account")

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Amount", amount, "been successfully withdrawn from the account")
        else:
            print("Insufficient funds on the account")

    def bank_fees(self):
        self.balance *= 0.95

    def display(self):
        print("Account number:", self.account_number)
        print("Name:", self.name)
        print("Balance:", self.balance)

    # Added an extra method to make it more fun
    def authorize(self):
        account_number = int(input("Enter account number: "))
        password = input("Enter password: ")
        if account_number == self.account_number and password == self.password:
            return True
        else:
            print("Invalid account number or password")
            return False


# Creating an object of class BankAccount
account = bank_account(944567, "Krupin Dmitriy", 200000, "12345")

# User authorization
while not account.authorize():
    pass

# Checking the methods of the BankAccount class
account.display()  # Displaying account information
account.deposit(int(input("Enter the replenishment amount: ")))  # Adding to account balance
account.withdrawal(int(input("Enter the amount to withdraw: ")))  # Withdrawal of funds from the account
account.bank_fees()  # Application of bank fees
account.display()  # Displaying updated account information
